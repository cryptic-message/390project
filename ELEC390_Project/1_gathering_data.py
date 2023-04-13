# ELEC390 Project: Taking raw data into combined csv files
import numpy as np
import h5py as h
import pandas as pd
import matplotlib.pyplot as plt

# import datasets

# import jumping data
jds1 = pd.read_csv("../data_collection/curtis_data/back pocket jumping/Raw Data.csv", delimiter='\t')
jds2 = pd.read_csv("../data_collection/curtis_data/front pocket jumping/Raw Data.csv", delimiter='\t')
jds3 = pd.read_csv("../data_collection/curtis_data/hand jumping/Raw Data.csv", delimiter='\t')
# jds4 = pd.read_csv("../data_collection/nicholas_data/jumping/phone_horizontal_jumping/Raw Data.csv", delimiter='\t')

# combine jumping data into one dataframe
jd = np.empty((1, 5), dtype=float)

jd = np.vstack([jd, jds1])
jd = np.vstack([jd, jds2])
jd = np.vstack([jd, jds3])

cols = ["Time (s)", "Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
jdf = pd.DataFrame(jd, columns=cols)
jdf["Label"] = 1


# import walking data
wds1 = pd.read_csv("../data_collection/curtis_data/back pocket walking/Raw Data.csv", delimiter='\t')
wds2 = pd.read_csv("../data_collection/curtis_data/front pocket walking/Raw Data.csv", delimiter='\t')
wds3 = pd.read_csv("../data_collection/curtis_data/hand walking/Raw Data.csv", delimiter='\t')

# combine jumping data into one dataframe
wd = np.empty((1, 5), dtype=float)

wd = np.vstack([wd, wds1])
wd = np.vstack([wd, wds2])
wd = np.vstack([wd, wds3])

cols = ["Time (s)", "Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)"]
wdf = pd.DataFrame(wd, columns=cols)
wdf["Label"] = 0

# stack wdf and jdf

df = np.vstack([wdf, jdf])

cols = ["Time (s)", "Linear Acceleration x (m/s^2)", "Linear Acceleration y (m/s^2)", "Linear Acceleration z (m/s^2)", "Absolute acceleration (m/s^2)","Label"]
df = pd.DataFrame(df, columns=cols)

print(df)

plt.plot(df.iloc[:, 0], df.iloc[:, 4])

plt.show()



