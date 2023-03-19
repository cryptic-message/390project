# ELEC390 Project test
import numpy as np
import h5py as h
import pandas as pd
import matplotlib.pyplot as plt

dataset1 = pd.read_csv("../DataCollection/Curtis/hand walking/Raw Data.csv", delimiter='\t')

data1 = dataset1.iloc[:, 0:5]

# print(data1)

# writing to h5 file
# open the h5 file in write mode
with h.File('../hdf5_file.h5', 'w') as hdf:
    Member1Curtis = hdf.create_group('/Member1Curtis')
    Member1Curtis.create_dataset('hand_walking', data=data1)

    Test = hdf.create_group('/Dataset/Test')
    Train = hdf.create_group('/Dataset/Train')

# reading from h5 file
# open the h5 file in read mode
with h.File('../hdf5_file.h5','r') as hdf:
    ls = list(hdf.keys())
    print(ls)
    # print dataset 1
    d1 = hdf.get('Member1Curtis/hand_walking')
    array1 = np.array(d1)
    print(array1)
