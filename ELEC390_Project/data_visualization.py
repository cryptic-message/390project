import pandas as pd
import h5py as h
import matplotlib.pyplot as plt
import numpy as np

# open the h5 file in read-only mode
with h.File('../hdf5_data.h5', 'r') as hdf:
    walking_training = hdf.get('dataset/Train/walking_training')
    array1 = np.array(walking_training)
    print(array1)

plt.subplots(nrows=1, ncols=5, sharex=True)
plt.plot(array1[:,0], array1[:,1])
plt.show()