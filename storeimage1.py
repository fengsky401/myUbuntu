#coding:utf-8
from PIL import Image
import cPickle
import os
import numpy
import time
import scipy


from pylab import *

#class LoadImageFile()


indir1="/home/queenie/图片/footballimage"
for (root,dirs,filenames) in os.walk(indir1):
    for i,f in enumerate(filenames):
      try:
         print f
         file=open('datafootball.pkl','wb')
         im=array(Image.open(os.path.join(root,f)).convert('L'))
         #Ima=im.load()
         #Image=numpy.asarray(Ima)
         cPickle.dump(im,file)
         #print Image
         file.close()
         print i+1,
         print "success"
      except IOError:
         continue

#file=open('datafootball.pkl','wb')
#image=cPickle.load(file)
#print image
