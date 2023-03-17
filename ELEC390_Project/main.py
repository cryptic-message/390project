# ELEC390 Project test
import numpy as np
import h5py as h

print("howdy-doo")

# create random matrices
m1 = np.random.random(size=(1000, 1000))
m2 = np.random.random(size=(10, 10))

# writing to h5 file
# open the h5 file in write mode
with h.File('./hdf5_data_test.h5','w') as hdf:
    hdf.create_dataset('dataset1', data=m1)
    hdf.create_dataset('dataset2', data=m2)

# reading from h5 file
# open the h5 file in read mode
with h.File('./hdf5_data_test.h5','r') as hdf:
    ls = list(hdf.keys())
    print(ls)
    # print dataset 1
    data1 = hdf.get('dataset1')
    array1 = np.array(data1)
    print(array1)
    # print dataset 2
    data2 = hdf.get('dataset2')
    array2 = np.array(data2)
    print(array2)
