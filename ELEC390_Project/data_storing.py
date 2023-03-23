import pandas as pd
import h5py as h

# load the shuffled split data
jumping_training = pd.read_csv('../data_collection/jumping_shuffle_training.csv')
jumping_testing = pd.read_csv('../data_collection/jumping_shuffle_testing.csv')
walking_training = pd.read_csv('../data_collection/walking_shuffle_training.csv')
walking_testing = pd.read_csv('../data_collection/walking_shuffle_testing.csv')

with h.File('../hdf5_data.h5','w') as hdf:
    Train = hdf.create_group('/dataset/Train')
    Test = hdf.create_group('/dataset/Test')

    # add training datasets
    Train.create_dataset('jumping_training', data=jumping_training)
    Train.create_dataset('walking_training', data=walking_training)

    # add testing datasets
    Test.create_dataset('jumping_testing', data=jumping_testing)
    Test.create_dataset('walking_testing', data=walking_testing)
