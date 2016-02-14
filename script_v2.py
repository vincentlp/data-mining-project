import os
import numpy as np
import csv
import pandas as pd
from sklearn import svm
from sklearn import datasets
from sklearn.cross_validation import KFold
from sklearn.tree import DecisionTreeRegressor



#on definit le dossier de travail
os.chdir("/homes/fviossat/Bureau/ISA/403_Fouille_de_donnees/Data_Kaggle")
test_directory = os.getcwd()
print "Current working directory %s" % test_directory


#X_train correspond a train_predictors.csv et Y_train a train_response.csv

X_train = pd.read_csv(open("train_predictors.csv"), sep=';')
#print X_train.head()

Y_train = pd.read_csv(open("train_response.csv"), sep=';')
#print Y_train.head()

X_test = pd.read_csv(open("test_modif.csv"), sep=';')
#print X_test.head()



#Ecrit dans un fichier txt le nbre de modalites pour les variables categorielles
file = open("nombre_modalites.txt", "w")
file.write("Nombre de modalites de la variable %s: %d" % ('Product_Info_1',len(X_train['Product_Info_1'].unique()))
+"\n" +  "Nombre de modalites de la variable %s: %d" % ('Product_Info_2',len(X_train['Product_Info_2'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Product_Info_3',len(X_train['Product_Info_3'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Product_Info_5',len(X_train['Product_Info_5'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Product_Info_6',len(X_train['Product_Info_6'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Product_Info_7',len(X_train['Product_Info_7'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Employment_Info_2',len(X_train['Employment_Info_2'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Employment_Info_3',len(X_train['Employment_Info_3'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Employment_Info_5',len(X_train['Employment_Info_5'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_1',len(X_train['InsuredInfo_1'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_2',len(X_train['InsuredInfo_2'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_3',len(X_train['InsuredInfo_3'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_4',len(X_train['InsuredInfo_4'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_5',len(X_train['InsuredInfo_5'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_6',len(X_train['InsuredInfo_6'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('InsuredInfo_7',len(X_train['InsuredInfo_7'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Insurance_History_1',len(X_train['Insurance_History_1'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Insurance_History_2',len(X_train['Insurance_History_2'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Insurance_History_3',len(X_train['Insurance_History_3'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Insurance_History_4',len(X_train['Insurance_History_4'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Insurance_History_7',len(X_train['Insurance_History_7'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Insurance_History_8',len(X_train['Insurance_History_8'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Insurance_History_9',len(X_train['Insurance_History_9'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Family_Hist_1',len(X_train['Family_Hist_1'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_2',len(X_train['Medical_History_2'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_3',len(X_train['Medical_History_3'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_4',len(X_train['Medical_History_4'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_5',len(X_train['Medical_History_5'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_6',len(X_train['Medical_History_6'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_7',len(X_train['Medical_History_7'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_8',len(X_train['Medical_History_8'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_9',len(X_train['Medical_History_9'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_11',len(X_train['Medical_History_11'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_12',len(X_train['Medical_History_12'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_13',len(X_train['Medical_History_13'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_14',len(X_train['Medical_History_14'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_16',len(X_train['Medical_History_16'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_17',len(X_train['Medical_History_17'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_18',len(X_train['Medical_History_18'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_19',len(X_train['Medical_History_19'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_20',len(X_train['Medical_History_20'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_21',len(X_train['Medical_History_21'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_22',len(X_train['Medical_History_22'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_23',len(X_train['Medical_History_23'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_25',len(X_train['Medical_History_25'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_26',len(X_train['Medical_History_26'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_27',len(X_train['Medical_History_27'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_28',len(X_train['Medical_History_28'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_29',len(X_train['Medical_History_29'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_30',len(X_train['Medical_History_30'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_31',len(X_train['Medical_History_31'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_33',len(X_train['Medical_History_33'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_34',len(X_train['Medical_History_34'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_35',len(X_train['Medical_History_35'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_36',len(X_train['Medical_History_36'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_37',len(X_train['Medical_History_37'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_38',len(X_train['Medical_History_38'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_39',len(X_train['Medical_History_39'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_40',len(X_train['Medical_History_40'].unique()))
+"\n" + "Nombre de modalites de la variable %s: %d" % ('Medical_History_41',len(X_train['Medical_History_41'].unique()))
+"\n" + "Nombre de modalites de la variable discrete %s: %d" % ('Medical_History_1',len(X_train['Medical_History_11'].unique()))
+"\n" + "Nombre de modalites de la variable discrete %s: %d" % ('Medical_History_10',len(X_train['Medical_History_10'].unique()))
+"\n" + "Nombre de modalites de la variable discrete %s: %d" % ('Medical_History_15',len(X_train['Medical_History_15'].unique()))
+"\n" + "Nombre de modalites de la variable discrete %s: %d" % ('Medical_History_24',len(X_train['Medical_History_24'].unique()))
+"\n" + "Nombre de modalites de la variable discrete %s: %d" % ('Medical_History_32',len(X_train['Medical_History_32'].unique())))
file.close()



#Dummisation
list_dummies = ['Product_Info_1','Product_Info_2','Product_Info_3', 'Product_Info_5', 'Product_Info_6', 'Product_Info_7', 'Employment_Info_2', 'Employment_Info_3', 'Employment_Info_5', 'InsuredInfo_1', 'InsuredInfo_2', 'InsuredInfo_3', 'InsuredInfo_4', 'InsuredInfo_5', 'InsuredInfo_6', 'InsuredInfo_7', 'Insurance_History_1', 'Insurance_History_2', 'Insurance_History_3', 'Insurance_History_4', 'Insurance_History_7', 'Insurance_History_8', 'Insurance_History_9', 'Family_Hist_1', 'Medical_History_2', 'Medical_History_3', 'Medical_History_4', 'Medical_History_5', 'Medical_History_6', 'Medical_History_7', 'Medical_History_8', 'Medical_History_9', 'Medical_History_11', 'Medical_History_12', 'Medical_History_13', 'Medical_History_14', 'Medical_History_16', 'Medical_History_17', 'Medical_History_18', 'Medical_History_19', 'Medical_History_20', 'Medical_History_21', 'Medical_History_22', 'Medical_History_23', 'Medical_History_25', 'Medical_History_26', 'Medical_History_27', 'Medical_History_28', 'Medical_History_29', 'Medical_History_30', 'Medical_History_31', 'Medical_History_33', 'Medical_History_34', 'Medical_History_35', 'Medical_History_36', 'Medical_History_37', 'Medical_History_38', 'Medical_History_39', 'Medical_History_40', 'Medical_History_41', 'Medical_History_1', 'Medical_History_10', 'Medical_History_15', 'Medical_History_24', 'Medical_History_32']
for v in list_dummies:
    dummies = pd.get_dummies(X_train[v], prefix=v+"_")
    X_train = pd.concat([X_train, dummies], axis=1)
    del X_train[v]
pd.set_option('max_columns', None)
#print X_train.head()



#Description des variables continues
file = open("description_var_continues.txt", "w")
file.write(str(X_train[['Id','Product_Info_4', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1', 'Employment_Info_4', 'Employment_Info_6', 'Insurance_History_5', 'Family_Hist_2', 'Family_Hist_3', 'Family_Hist_4', 'Family_Hist_5']].describe()))
file.close()



#On lance le premier arbre
model = DecisionTreeRegressor()
model.fit(X_train, Y_train) # On fit le modele sur le training set
Y_test = model.predict(X_test) # On effectue les predictions sur le test set









