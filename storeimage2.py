#coding:utf-8

import os,sys
import numpy
import time
import scipy
import gzip
import shutil
from PIL import Image
import cPickle
import cv2
from pylab import *


def listdir(imgset,tarset,dataset,dir,logfile):
    print (dir+'\n')
    filenum=0
    list=os.listdir(dir)
    for line in list:
        filepath=os.path.join(dir,line)
        if os.path.isdir(filepath):
           print "%s:"%(filepath)
        for li in os.listdir(filepath):
            try:
               
                 ima=array(Image.open(os.path.join(line,li)).convert('L').resize((50,50)))
                 im=ima.reshape((1,2500))
                 cv2.normalize(im,im,0,255,cv2.NORM_MINMAX)
                 im=numpy.float32(im)/255
                 imgset.append(im)
                 target=1  if 'f' in f else 0
                 tarset.append(target)
                 logfile.write(filenum+' '+os.path.join(filepath,li)+ '\n')
                 filenum+=1
            except IOError:
                 continue
    imgset=numpy.asarray(imgset)
    imgset=imgset.reshape((imgset.size)/2500,2500)
    dataset.append(imgset)
    dataset.append(array(tarset))



file=open('trainplankton.pkl','wb')                 
trainset_img=[]
trainset_tar=[]
trainset=[]
indir1="/home/queenie/图片/zooplanktonimage/train"
logfile=open('list.txt','w')
listdir(trainset_img,trainset_tar,trainset,indir1,file)
print trainset
