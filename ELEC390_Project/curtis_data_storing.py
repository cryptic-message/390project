# ELEC390 Project test
import numpy as np
import h5py as h
import pandas as pd
import matplotlib.pyplot as plt

dataset1 = pd.read_csv("../data_collection/curtis_data/back pocket walking/Raw Data.csv", delimiter='\t')
dataset2 = pd.read_csv("../data_collection/curtis_data/back pocket jumping/Raw Data.csv", delimiter='\t')
dataset3 = pd.read_csv("../data_collection/curtis_data/front pocket jumping/Raw Data.csv", delimiter='\t')
dataset4 = pd.read_csv("../data_collection/curtis_data/front pocket walking/Raw Data.csv", delimiter='\t')
dataset5 = pd.read_csv("../data_collection/curtis_data/hand jumping/Raw Data.csv", delimiter='\t')
dataset6 = pd.read_csv("../data_collection/curtis_data/hand walking/Raw Data.csv", delimiter='\t')

data1 = dataset1.iloc[:, 0:5]
data2 = dataset2.iloc[:, 0:5]
data3 = dataset3.iloc[:, 0:5]
data4 = dataset4.iloc[:, 0:5]
data5 = dataset5.iloc[:, 0:5]
data6 = dataset6.iloc[:, 0:5]

# print(data1)

# writing to h5 file
# open the h5 file in write mode
with h.File('../hdf5_file.h5', 'w') as hdf:
    Member1Curtis = hdf.create_group('/Member1Curtis')
    Member1Curtis.create_dataset('back_pocket_walking', data=data1)
    Member1Curtis.create_dataset('back_pocket_jumping', data=data2)
    Member1Curtis.create_dataset('front_pocket_jumping', data=data3)
    Member1Curtis.create_dataset('front_pocket_walking', data=data4)
    Member1Curtis.create_dataset('hand_jumping', data=data5)
    Member1Curtis.create_dataset('hand_walking', data=data6)
    Test = hdf.create_group('/dataset/Test')
    Train = hdf.create_group('/dataset/Train')

for i in range(0,12)
    d = dataset1.iloc[]
