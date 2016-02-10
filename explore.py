#!/usr/bin/python
# coding: latin-1
import os, sys

import pandas as pd
import numpy as np
from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
import csv
import matplotlib as plt
import matplotlib.pyplot
import seaborn as sns
sns.set_style('whitegrid')
sns.color_palette("RdBu", n_colors=7)


train = pd.read_csv(open('data/train.csv','rb'), sep=',')
test = pd.read_csv(open('data/test.csv', 'rb'), sep=',')

# ######## TRAIN ########

# print train.columns
# print train.describe()
print train.head(5)

# Looking at Response
sns.countplot(x='Response', data=train, palette="RdBu", order=range(1,9))
plt.pyplot.show()

# Size of dataset : nrows : 59381, ncols : 128
print("train: nrows %d, ncols %d" % train.shape)

# List features with missing values
print("%20s \tCount \tPct missing" % 'Feature')
for column_name, column in train.transpose().iterrows():
	naCount = sum(column.isnull())
	if naCount > 0:
		print("%20s`\t%5d \t%2.2f%%" % (column_name, naCount, 100.*naCount/train.shape[0]))

# fig = plt.pyplot.figure()
# ax = fig.add_subplot(111)
# ax.hist(train['Response'], bins = 10, range = (train['Response'].min(),train['Response'].max()))
# plt.pyplot.title('Response distribution')
# plt.pyplot.xlabel('Response')
# plt.pyplot.ylabel('Count')