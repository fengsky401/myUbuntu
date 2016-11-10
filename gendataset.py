import numpy
from os import listdir
from os.path import isfile,join

import h5py
import numpy
from scipy import misc
from scipy.misc import imsave 
rng=numpy.random.RandomState(123522)


if __name__=="__main__":
    files=[f for f in listdir(join('train'))
           if isfile(join('train',f))]
    rng.shuffle(files)
    
    f=h5py.File('gene_dataset.hdf5','w')
    dt=h5py.special_dtype(vlen=numpy.dtype('uint8'))
    features=f.create_dataset('images',(120000,),dtype=dt)
    shapes=f.create_dataset('shapes',(120000,3),dtype='uint16')
    targets=f.create_dataset('labels',(120000,),dtype='uint8')
   
    for i,f in enumerate(files):
        image=misc.imread(join('train',f))
        target=0 if 'foot' in f else 1
        features[i]=image.flatten()
        targets[i]=target
        shapes[i]=image.shape
        
        print 'success y2s',
        print targets[i],
        print features[i].shape[0],
        print x,
        print y
