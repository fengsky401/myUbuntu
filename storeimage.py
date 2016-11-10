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

trainset_img=[]
trainset_tar=[]
trainset=[]
file=open('trainplankton.pkl','wb')
logfile=open('trainplanktonlist.txt','wb')   
tarfile=open('trainplanktontar.txt','wb')   
indir1="/home/queenie/图片/zooplanktonimage/train"

for (root,dirs,filenames) in os.walk(indir1):
  
    for i,f in enumerate(filenames):
    
      try:
         
         ima=array(Image.open(os.path.join(root,f)).convert('L').resize((50,50)))
         
         #ima=asarray(image)
         im=ima.reshape((1,2500))
         
         
         cv2.normalize(im,im,0,255,cv2.NORM_MINMAX)
         im=numpy.float32(im)/255
         trainset_img.append(im)
         if 'acantharia_protist' in os.path.join(root,f):
             target=1
         elif 'acantharia_protist_halo' in os.path.join(root,f): 
             target=2 
         elif 'appendicularian_slight_curve' in os.path.join(root,f): 
             target=3
         elif 'appendicularian_s_shape' in os.path.join(root,f): 
             target=4
         elif 'appendicularian_straight' in os.path.join(root,f): 
             target=5
         elif 'artifacts' in os.path.join(root,f): 
             target=6
         elif 'chaetognath_non_sagitta' in os.path.join(root,f): 
             target=7
         elif 'chaetognath_other' in os.path.join(root,f):
             target=8
         elif 'chaetognath_sagitta' in os.path.join(root,f):
             target=9
         elif 'copepod_calanoid' in os.path.join(root,f):
             target=10
         elif 'copepod_calanoid_flatheads' in os.path.join(root,f):
             target=11
         
         elif 'copepod_calanoid_large' in os.path.join(root,f):
             target=12
         elif 'copepod_cyclopoid_oithona' in os.path.join(root,f):
             target=13
         elif 'copepod_cyclopoid_oithona_eggs' in os.path.join(root,f):
             target=14
         elif 'crustacean_other' in os.path.join(root,f):
             target=15
         elif 'detritus_blob' in os.path.join(root,f):
             target=16
         else:
             target=0
         trainset_tar.append(target)
        
         tarfile.write(str(target)+' ')
         
         logfile.write(os.path.join(root,f)+'\n')
      except IOError:
         continue
     
trainset_img=numpy.asarray(trainset_img)


trainset_img=trainset_img.reshape((trainset_img.size)/2500,2500)


trainset.append(trainset_img)

trainset.append(array(trainset_tar))
file.close()
logfile.close()
tarfile.close()
print trainset
print trainset_img.size
print array(trainset_tar).size

'''
#create validation dataset
validation_img=[]
validation_tar=[]
validset=[]
indir2="/home/queenie/autoencoder/valid"
print "validationset:"
for (root,dirs,filenames) in os.walk(indir2):
    for i,f in enumerate(filenames):
      try:
         
         file=open('datafootball.pkl','wb')
         ima=array(Image.open(os.path.join(root,f)).convert('L').resize((300,400)))
         
         im=ima.reshape((1,120000))
         cv2.normalize(im,im,0,255,cv2.NORM_MINMAX)
         im=numpy.float32(im)/255
         
         
         validation_img.append(im)
         target=1  if 'foot' in f else 0
         validation_tar.append(target)
        
         print i+1,
         print f
         
         
      except IOError:
         continue

validation_img=numpy.asarray(validation_img)
validation_img=validation_img.reshape(4,120000)


validset.append(validation_img)

validset.append(array(validation_tar))
print validset
print validation_img.size
print array(validation_tar).size

#create testset
testset_img=[]
testset_tar=[]
testset=[]
indir3="/home/queenie/autoencoder/test"
print "testset:"
for (root,dirs,filenames) in os.walk(indir3):
    for i,f in enumerate(filenames):
      try:
         
         file=open('datafootball.pkl','wb')
         ima=array(Image.open(os.path.join(root,f)).convert('L').resize((300,400)))
         
         im=ima.reshape((1,120000))
         cv2.normalize(im,im,0,255,cv2.NORM_MINMAX)
         im=numpy.float32(im)/255
         
         
         testset_img.append(im)
         target=1  if 'foot' in f else 0
         testset_tar.append(target)
        
         print i+1,
         print f
         
      except IOError:
         continue

testset_img=numpy.asarray(validation_img)
testset_img=testset_img.reshape(4,120000)


testset.append(testset_img)

testset.append(array(testset_tar))
print testset
print testset_img.size
print array(testset_tar).size



#create dataset
dataset=[]
dataset.append(trainset)
dataset.append(validset)
dataset.append(testset)

dataset=tuple(dataset)

file=open('datafootball.pkl','wb')
cPickle.dump(dataset,file)
file.close()

print "length of dataset:%s,length of trainset:%s,length of validation set:%s,length of test set:%s"%(len(dataset),len(trainset),len(validset),len(testset))
print dataset
with open('datafootball.pkl','rb') as f_in,gzip.open('datafootball.pkl.gz','wb') as f_out:
    shutil.copyfileobj(f_in,f_out)
print "all success"
'''
