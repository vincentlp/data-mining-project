#!/usr/bin/python
# coding: latin-1
import os, sys

import pandas as pd
import numpy as np
from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import Imputer
import csv

X = pd.read_csv(open('data/train_predictors.csv','rb'), sep=';')
# print data.head()
Y = pd.read_csv(open('data/train_response.csv', 'rb'), sep=';')
X_test = pd.read_csv(open('data/test_modif.csv', 'rb'), sep=';')

print "Nombre de modalites de la variable %s: %d" % ('Product_Info_1',len(X['Product_Info_1'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Product_Info_2',len(X['Product_Info_2'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Product_Info_3',len(X['Product_Info_3'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Product_Info_5',len(X['Product_Info_5'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Product_Info_6',len(X['Product_Info_6'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Product_Info_7',len(X['Product_Info_7'].unique()))

print "Nombre de modalites de la variable %s: %d" % ('Employment_Info_2',len(X['Employment_Info_2'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Employment_Info_3',len(X['Employment_Info_3'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Employment_Info_5',len(X['Employment_Info_5'].unique()))

print "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_1',len(X['InsuredInfo_1'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_2',len(X['InsuredInfo_2'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_3',len(X['InsuredInfo_3'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_4',len(X['InsuredInfo_4'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_5',len(X['InsuredInfo_5'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_6',len(X['InsuredInfo_6'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_7',len(X['InsuredInfo_7'].unique()))

print "Nombre de modalites de la variable %s: %d" % ('Insurance_History_1',len(X['Insurance_History_1'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Insurance_History_2',len(X['Insurance_History_2'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Insurance_History_3',len(X['Insurance_History_3'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Insurance_History_4',len(X['Insurance_History_4'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Insurance_History_7',len(X['Insurance_History_7'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Insurance_History_8',len(X['Insurance_History_8'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Insurance_History_9',len(X['Insurance_History_9'].unique()))

print "Nombre de modalites de la variable %s: %d" % ('Family_Hist_1',len(X['Family_Hist_1'].unique()))

print "Nombre de modalites de la variable %s: %d" % ('Medical_History_2',len(X['Medical_History_2'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_3',len(X['Medical_History_3'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_4',len(X['Medical_History_4'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_5',len(X['Medical_History_5'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_6',len(X['Medical_History_6'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_7',len(X['Medical_History_7'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_8',len(X['Medical_History_8'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_9',len(X['Medical_History_9'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_11',len(X['Medical_History_11'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_12',len(X['Medical_History_12'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_13',len(X['Medical_History_13'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_14',len(X['Medical_History_14'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_16',len(X['Medical_History_16'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_17',len(X['Medical_History_17'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_18',len(X['Medical_History_18'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_19',len(X['Medical_History_19'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_20',len(X['Medical_History_20'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_21',len(X['Medical_History_21'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_22',len(X['Medical_History_22'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_23',len(X['Medical_History_23'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_25',len(X['Medical_History_25'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_26',len(X['Medical_History_26'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_27',len(X['Medical_History_27'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_28',len(X['Medical_History_28'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_29',len(X['Medical_History_29'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_30',len(X['Medical_History_30'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_31',len(X['Medical_History_31'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_33',len(X['Medical_History_33'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_34',len(X['Medical_History_34'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_35',len(X['Medical_History_35'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_36',len(X['Medical_History_36'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_37',len(X['Medical_History_37'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_38',len(X['Medical_History_38'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_39',len(X['Medical_History_39'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_40',len(X['Medical_History_40'].unique()))
print "Nombre de modalites de la variable %s: %d" % ('Medical_History_41',len(X['Medical_History_41'].unique()))

print X.columns
print X_test.columns
X = X.drop('Product_Info_2', 1)
X_test = X_test.drop('Product_Info_2', 1)
print X.columns
print X_test.columns

# #dummisation
# list_dummies = ['Product_Info_1', 'Product_Info_2', 'Product_Info_3', 'Product_Info_5', 'Product_Info_6', 'Product_Info_7', 'Employment_Info_2', 'Employment_Info_3', 'Employment_Info_5', 'InsuredInfo_1', 'InsuredInfo_2', 'InsuredInfo_3', 'InsuredInfo_4', 'InsuredInfo_5', 'InsuredInfo_6', 'InsuredInfo_7', 'Insurance_History_1', 'Insurance_History_2', 'Insurance_History_3', 'Insurance_History_4', 'Insurance_History_7', 'Insurance_History_8', 'Insurance_History_9', 'Family_Hist_1', 'Medical_History_2', 'Medical_History_3', 'Medical_History_4', 'Medical_History_5', 'Medical_History_6', 'Medical_History_7', 'Medical_History_8', 'Medical_History_9', 'Medical_History_11', 'Medical_History_12', 'Medical_History_13', 'Medical_History_14', 'Medical_History_16', 'Medical_History_17', 'Medical_History_18', 'Medical_History_19', 'Medical_History_20', 'Medical_History_21', 'Medical_History_22', 'Medical_History_23', 'Medical_History_25', 'Medical_History_26', 'Medical_History_27', 'Medical_History_28', 'Medical_History_29', 'Medical_History_30', 'Medical_History_31', 'Medical_History_33', 'Medical_History_34', 'Medical_History_35', 'Medical_History_36', 'Medical_History_37', 'Medical_History_38', 'Medical_History_39', 'Medical_History_40', 'Medical_History_41']
# for v in list_dummies:
# 	dummies = pd.get_dummies(X[v], prefix=v+"_")
# 	X = pd.concat([X, dummies], axis=1)
# 	del X[v]
# pd.set_option('max_columns', None)
# # print X.head()
# print X.columns

new_X=Imputer().fit_transform(X)
new_X_test=Imputer().fit_transform(X_test)


# #splitting
# np.random.seed(seed=1234)
# ind_train = np.random.choice(len(new_X),0.5*len(new_X),replace=False)
# ind_val_test = list(set(range(len(new_X))) - set(ind_train))
# ind_val = np.random.choice(ind_val_test,0.7*len(ind_val_test),replace=False)
# ind_test = list(set(ind_val_test) - set(ind_val))
# new_X, X_val, X_test, Y, Y_val, Y_test = new_X.iloc[ind_train], new_X.iloc
# [ind_val], new_X.iloc[ind_test], Y.iloc[ind_train], Y.iloc[ind_val], Y.iloc[ind_test]


#modelling
model = DecisionTreeRegressor()
model.fit(new_X, Y) # On fit le modèle sur le training set
prediction = model.predict(new_X_test) # On effectue les prédictions sur le test set



def rmse(obs, pred):
	return np.sqrt(np.mean((obs-pred)**2))

rmse_train = rmse(Y, model.predict(new_X))
#rmse_test = rmse(Y_test, prediction)

print "Train Error: %.2f" % rmse_train
#print "Test Error: %.2f" % rmse_test

#print Y_test