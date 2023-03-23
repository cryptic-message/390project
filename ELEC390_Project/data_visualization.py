import pandas as pd
import h5py as h
import matplotlib.pyplot as plt
import numpy as np

# open the h5 file in read-only mode
with h.File('../hdf5_data.h5', 'r') as hdf:
    walking_training = hdf.get('dataset/Train/walking_training')
    array1 = np.array(walking_training)
    print(array1)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4,ncols=1)
ax1.plot(array1[:,0], array1[:,1])
ax2.plot(array1[:,0], array1[:,2])
ax3.plot(array1[:,0], array1[:,3])
ax4.plot(array1[:,0], array1[:,4])
plt.show()