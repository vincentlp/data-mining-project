#!/usr/bin/python
# coding: latin-1
import os, sys

import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
import csv
# import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
sns.color_palette("RdBu", n_colors=7)

# import pylab


# # numpy, matplotlib, seaborn
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_style('whitegrid')



train = pd.read_csv(open('data/train.csv','rb'), sep=',')
test = pd.read_csv(open('data/test.csv', 'rb'), sep=',')

# ######## TRAIN ########

# print train.columns
# print train.describe()
# print train.head(5)

# # Looking at Response
# sns.countplot(x='Response', data=train, palette="RdBu", order=range(1,9))
# plt.show()

# # Size of dataset : nrows : 59381, ncols : 128
# print("Train: number_of_rows %d, number_of_cols %d" % train.shape)


# # List features with missing values
# print("%20s \tCount \tPercentage missing" % 'Feature')
# for column_name, column in train.transpose().iterrows():
# 	naCount = sum(column.isnull())
# 	if naCount > 0:
# 		print("%20s`\t%5d \t%2.2f%%" % (column_name, naCount, 100.*naCount/train.shape[0]))




# # Plot distributions for Employment_Info_4 and Employment_Info_6

# fig, (axis1,axis2) = plt.subplots(1,2,figsize=(15,4))
# train["Employment_Info_4"].plot(kind='hist',bins=50,xlim=(0,1),ax=axis1, color="red")
# axis1.set_xlabel("Employment_Info_4")
# axis1.set_ylabel("Count")
# train["Employment_Info_6"].plot(kind='hist',bins=50,xlim=(0,1),ax=axis2, color="red")
# axis2.set_xlabel("Employment_Info_6")
# axis2.set_ylabel("Count")

# plt.show()


# List all of the Insurance_History_5 values greater than 0.02  (Max is 1.0)
print train["Insurance_History_5"][train["Insurance_History_5"]>0.03]

fig, axis1 = plt.subplots(1,1,figsize=(20,5))
train["Insurance_History_5"][train["Insurance_History_5"]<0.034].plot(kind='hist',bins=100,xlim=(0,0.05),ax=axis1, color="blue")
axis1.set_xlabel("Insurance_History_5")
axis1.set_ylabel("Count")
plt.show()

# fig = plt.pyplot.figure()
# ax = fig.add_subplot(111)
# ax.hist(train['Response'], bins = 10, range = (train['Response'].min(),train['Response'].max()))
# plt.pyplot.title('Response distribution')
# plt.pyplot.xlabel('Response')
# plt.pyplot.ylabel('Count')