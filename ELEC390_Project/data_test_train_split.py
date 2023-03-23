import pandas as pd
import random as rand
import math

jumping_shuffle = pd.read_csv('../data_collection/jumping_shuffle.csv')
walking_shuffle = pd.read_csv('../data_collection/walking_shuffle.csv')

print(jumping_shuffle)
print(walking_shuffle)

print(jumping_shuffle.iloc[0:1, :])

# split the data into training and testing
jumping_training = pd.DataFrame()
jumping_testing = pd.DataFrame()
walking_training = pd.DataFrame()
walking_testing = pd.DataFrame()

jumping_training = jumping_shuffle.iloc[0:math.floor(len(jumping_shuffle)*0.9), :]
jumping_testing = jumping_shuffle.iloc[math.floor(len(jumping_shuffle)*0.9)+1:, :]
walking_training = walking_shuffle.iloc[0:math.floor(len(jumping_shuffle)*0.9), :]
walking_testing = walking_shuffle.iloc[math.floor(len(jumping_shuffle)*0.9)+1:, :]

print(jumping_training)
print(jumping_testing)
print(walking_training)
print(walking_testing)

jumping_training.to_csv('../data_collection/jumping_shuffle_training.csv', index=False)
jumping_testing.to_csv('../data_collection/jumping_shuffle_testing.csv', index=False)
walking_training.to_csv('../data_collection/walking_shuffle_training.csv', index=False)
walking_testing.to_csv('../data_collection/walking_shuffle_testing.csv', index=False)

print("done")
