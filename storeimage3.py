#coding:utf-8

#Filname:storeimage.py
from PIL import Image
import cPickle
import os
import numpy
import time
import scipy
import gzip
import shutil


import cv2
from pylab import *

#class LoadImageFile()
def makedatacPickle(indir1,tarfile,logfile):
    dataset_img=[]
    dataset_tar=[]
    dataset=[]
    for (root,dirs,filenames) in os.walk(indir1):
  
     for i,f in enumerate(filenames):
    
       try:
         ima=array(Image.open(os.path.join(root,f)).convert('L').resize((28,28)))
         #ima=array(Image.open(os.path.join(root,f)).convert('L').resize((50,50)))
         
         #ima=asarray(image)
         #im=ima.reshape((1,2500))
         im=ima.reshape((1,28*28))
         
         cv2.normalize(im,im,0,255,cv2.NORM_MINMAX)
         im=numpy.float32(im)/255
         dataset_img.append(im)
         if 'Appendicularia' in os.path.join(root,f):
             target=1
         elif 'Bubble' in os.path.join(root,f): 
             target=2 
         elif 'Chaetognatha' in os.path.join(root,f): 
             target=3
         elif 'CladoceraPenilia' in os.path.join(root,f): 
             target=4
         elif 'Copepoda' in os.path.join(root,f): 
             target=5
         elif 'Decapoda' in os.path.join(root,f): 
             target=6
         elif 'Doliolida' in os.path.join(root,f): 
             target=7
         elif 'Egg' in os.path.join(root,f):
             target=8
         elif 'Fiber' in os.path.join(root,f):
             target=9
         #elif 'Gelatinous' in os.path.join(root,f):
             target=10
         #elif 'Multiple' in os.path.join(root,f):
             target=11
         
         #elif 'Nonbio' in os.path.join(root,f):
             target=12
         #elif 'Pteropoda' in os.path.join(root,f):
             target=13
         #elif 'copepod_cyclopoid_oithona_eggs' in os.path.join(root,f):
         #    target=14
         #elif 'crustacean_other' in os.path.join(root,f):
         #    target=15
         #elif 'detritus_blob' in os.path.join(root,f):
         #    target=16
         else:
             target=0
         dataset_tar.append(target)
        
         tarfile.write(str(target)+' '+os.path.join(root,f)+'\n')
         
         logfile.write(os.path.join(root,f)+'\n')
       except IOError:
         continue
    dataset_img=numpy.asarray(dataset_img)
    dataset_img=dataset_img.reshape((dataset_img.size)/784,28*28)
    dataset.append(dataset_img)
    dataset.append(array(dataset_tar))
    
    return dataset

dataset=[]
trainset=[]
validset=[]
testset=[]
file=open('trainplankton.pkl','wb')
logfile=open('trainplanktonlist.txt','wb')   
tarfile=open('trainplanktontar.txt','wb')  
datasetfile=open('trainplanktondataset.txt','wb') 
indir1="/home/queenie/图片/13/Training_Set"
trainset=makedatacPickle(indir1,tarfile,logfile)
datasetfile.write(str(trainset)+'\n')
print trainset

indir2="/home/queenie/图片/13/Validation_Set"
validset=makedatacPickle(indir2,tarfile,logfile)
datasetfile.write(str(validset)+'\n')
print validset

indir3="/home/queenie/图片/13/Test_Set"
testset=makedatacPickle(indir3,tarfile,logfile)
datasetfile.write(str(testset)+'\n')
print testset

dataset=[]
dataset.append(trainset)
dataset.append(validset)
dataset.append(testset)

dataset=tuple(dataset)
cPickle.dump(dataset,file)
file.close()
logfile.close()
tarfile.close()
datasetfile.close()
print dataset
with open('trainplankton.pkl','rb') as f_in,gzip.open('trainplankton.pkl.gz','wb') as f_out:
    shutil.copyfileobj(f_in,f_out)
print "all success"

