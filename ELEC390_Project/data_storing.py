import pandas as pd
import random as rand

all_jumping_data = pd.read_csv("../data_collection/all_jumping_data.csv", delimiter='\t')
print(all_jumping_data.iloc[:, 0:5])

prev_time = 0
prev_index = 0
temp_data = pd.DataFrame()
all_jumping_data_temp = temp_data

for i in range(len(all_jumping_data)):
    if all_jumping_data.loc[i,'Time (s)'] - prev_time >= 5 and all_jumping_data.loc[i+1, 'Time (s)'] > prev_time:
        if rand.randint(0,1)==1:
            all_jumping_data_temp = pd.concat([all_jumping_data_temp[:], all_jumping_data.loc[prev_index:i]])
            print("front")
        else:
            all_jumping_data_temp = pd.concat([all_jumping_data_temp.loc[prev_index:i], all_jumping_data_temp[:]])
            print("back")
        temp_data = []
        prev_index = i+1
        prev_time = all_jumping_data.loc[i, 'Time (s)']

    if float(all_jumping_data.loc[i, 'Time (s)']) - prev_time < 0:
        prev_time = all_jumping_data.loc[i, 'Time (s)']

all_walking_data = pd.read_csv("../data_collection/all_walking_data.csv", delimiter='\t')
print(all_walking_data.iloc[:, 0:5])

prev_time = 0
prev_index = 0
temp_data = pd.DataFrame()
all_walking_data_temp = temp_data

for i in range(len(all_walking_data)):
    if all_walking_data.loc[i,'Time (s)'] - prev_time >= 5 and all_walking_data.loc[i+1, 'Time (s)'] > prev_time:
        if rand.randint(0,1)==1:
            all_walking_data_temp = pd.concat([all_walking_data_temp[:], all_walking_data.loc[prev_index:i]])
            print("front")
        else:
            all_walking_data_temp = pd.concat([all_walking_data_temp.loc[prev_index:i], all_walking_data_temp[:]])
            print("back")
        temp_data = []
        prev_index = i+1
        prev_time = all_walking_data.loc[i, 'Time (s)']

    if float(all_walking_data.loc[i, 'Time (s)']) - prev_time < 0:
        prev_time = all_walking_data.loc[i, 'Time (s)']

all_jumping_data_temp.to_csv('../data_collection/jumping_shuffle.csv', index=False)
all_walking_data_temp.to_csv('../data_collection/walking_shuffle.csv', index=False)
