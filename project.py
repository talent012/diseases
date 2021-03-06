# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kkEKwLNbDMQE8LwXRfer7SM_UzDO36Ar

1.   Talent Mususa R195886Z
2.   Nivel Tore R195904G
3.   ChiedzaMusingarimi R197970R
"""

#Mounting drive

from google.colab import drive 
drive.mount('/content/drive', force_remount=True)

# Commented out IPython magic to ensure Python compatibility.
#importing libraries

import numpy as np
from numpy import array
import pandas as pd 
import matplotlib.pylab as plt
# %matplotlib inline
from matplotlib.colors import ListedColormap
import seaborn as sns
import missingno as ms
import os
from tkinter import *
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.metrics import confusion_matrix, classification_report

#Reading and extracting data 

dataset_1=pd.read_csv('/content/drive/MyDrive/project/data.csv')

#printing out the dataset

dataset_1

#inserting dataset into dataframe

data = pd.DataFrame({'Disease':['Covid','Cancer','Ebola','lassa fever', 'Sars', 'Zika'],
                      'Symptom_1':['headaches',np.nan,'headaches','headaches',np.nan,np.nan],
                      'Symptom_2':['vomiting','vomiting','vomiting','vomiting','vomiting',np.nan],
                      'Symptom_3':['shortness of breath','shortness of breath',np.nan,'shortness of breath',np.nan,'shortness of breath'],
                      'Symptom_4':['fatigure','fatigure','fatigure','fatigure','fatigure','fatigure'],
                      'Symptom_5':['sore throat','sore throat','sore throat','sore throat','sore throat','sore throat'],
                      'Symptom_6':['nausea','nausea','nausea','nausea','nausea',np.nan],
                      'Symptom_7':['chest pains','chest pains','chest pains','chest pains','chest pains',np.nan],
                      'Symptom_8':['muscel pain',np.nan,'muscel pain','muscel pain','muscel pain','muscel pain'],
                      'Symptom_9':[np.nan,'itching','itching','itching','itching','itching'],
                      'Symptom_10':['sore throat','sore throat','sore throat','sore throat','sore throat','sore throat'],
                      'Symptom_11':['stomach pain',np.nan,'stomach pain','stomach pain','stomach pain','stomach pain'],
                      'Symptom_12':['chills','chills',np.nan,'chills','chills','chills'],
                      'Symptom_13':['loss of weight','loss of weight','loss of weight','loss of weight','loss of weight','loss of weight'],
                      'Symptom_14':[np.nan,'hair loss','hair loss','hair loss','hair loss','hair loss'],
                      'Symptom_15':['appetite loss','appetite loss','appetite loss','appetite loss','appetite loss','appetite loss'],
                      'Symptom_16':['high temperature','high temperature','high temperature','high temperature','high temperature','high temperature'],
                      'Symptom_17':[np.nan,'coldness','coldness','coldness','coldness','coldness'],
                      })

#printing out the dataset

data

#Joining datasets

dataset_2 = pd.concat([dataset_1,data])

#printing out the dataset

dataset_2

#checking dataset shape

dataset_2.shape

#checking datatypes

dataset_2.info()

#checking the health of the data to check if there are blank spaces
ms.matrix(dataset_2)

dataset_2.dropna(how='all')

#dropping and replacing nan values
dataset_3 = dataset_2.fillna(value = 'Blank')
dataset_3

#checking the health of the data to check if there still any blank spaces
ms.matrix(dataset_3)

#checking unique values in Disease column

dataset_3['Disease'].unique()

#checking number of unique value 

dataset_3['Disease'].nunique()

dataset_3.replace({'Disease':{
 'Fungal infection':100,
 'Allergy':101,
 'GERD':102,
 'Chronic cholestasis':103,
 'Drug Reaction':104,
 'Peptic ulcer diseae':105,
 'AIDS':106,
 'Diabetes':107,
 'Gastroenteritis':108,
 'Bronchial Asthma':109,
 'Hypertension ':110,
 'Migraine':111,
 'Cervical spondylosis':112,
 'Paralysis (brain hemorrhage)':113,
 'Jaundice':114,
 'Malaria':115,
 'Chicken pox':116,
 'Dengue':117,
 'Typhoid':118,
 'hepatitis A':119,
 'Hepatitis B':120,
 'Hepatitis C':121,
 'Hepatitis D':122,
 'Hepatitis E':123,
 'Alcoholic hepatitis':124,
 'Tuberculosis':125,
 'Common Cold':127,
 'Pneumonia':128,
 'Dimorphic hemmorhoids(piles)':129,
 'Heart attack':130,
 'Varicose veins':131,
 'Hypothyroidism':132,
 'Hyperthyroidism':133,
 'Hypoglycemia':134,
 'Osteoarthristis':135,
 'Arthritis':136,
 '(vertigo) Paroymsal  Positional Vertigo':137,
 'Acne':137,
 'Urinary tract infection':138,
 'Psoriasis':139,
 'Impetigo':140,'Covid':141,
       'Cancer':142, 'Ebola':143, 'lassa fever':144, 'Sars':145, 'Zika':146,}},inplace=True)

dataset_3['Symptom_1'].unique()

#Encoding symptoms columns 
dataset_3['Symptom_1'],_=pd.factorize(dataset_2['Symptom_1'])
dataset_3['Symptom_2'],_=pd.factorize(dataset_2['Symptom_2'])
dataset_3['Symptom_3'],_=pd.factorize(dataset_2['Symptom_3'])
dataset_3['Symptom_4'],_=pd.factorize(dataset_2['Symptom_4'])
dataset_3['Symptom_5'],_=pd.factorize(dataset_2['Symptom_5'])
dataset_3['Symptom_6'],_=pd.factorize(dataset_2['Symptom_6'])
dataset_3['Symptom_7'],_=pd.factorize(dataset_2['Symptom_7'])
dataset_3['Symptom_8'],_=pd.factorize(dataset_2['Symptom_8'])
dataset_3['Symptom_9'],_=pd.factorize(dataset_2['Symptom_9'])
dataset_3['Symptom_10'],_=pd.factorize(dataset_2['Symptom_10'])
dataset_3['Symptom_11'],_=pd.factorize(dataset_2['Symptom_11'])
dataset_3['Symptom_12'],_=pd.factorize(dataset_2['Symptom_12'])
dataset_3['Symptom_13'],_=pd.factorize(dataset_2['Symptom_13'])
dataset_3['Symptom_14'],_=pd.factorize(dataset_2['Symptom_14'])
dataset_3['Symptom_15'],_=pd.factorize(dataset_2['Symptom_15'])
dataset_3['Symptom_16'],_=pd.factorize(dataset_2['Symptom_16'])
dataset_3['Symptom_17'],_=pd.factorize(dataset_2['Symptom_17'])

dataset_3

#checking datatypes
dataset_3.info()

#converting disease to numeric
dataset_3['Disease'] = pd.to_numeric(dataset_3['Disease'], errors = 'coerce')
dataset_3.loc[dataset_1['Disease'].isna()==True]
dataset_3

dataset_3.info()

#describing dataset
dataset_3.describe()

# distribution for tenure.
sns.distplot(dataset_3['Disease']);

#relation using correlation matrix
dataset_3.corr().style.background_gradient(cmap='PRGn_r')

#plotting a heatmap
plt.figure(figsize=(20,10))
sns.heatmap(dataset_3.corr(),annot=True,cmap='PRGn_r')

#showing symptoms that are most frquent to the diseases
corr_matrix = dataset_3.corr() 
corr_matrix 

corr_matrix['Disease'].sort_values(ascending=False)

#Visualising the effects of Symptom1 one to diseases
dataset_3.plot(kind='scatter',x='Disease',y='Symptom_1',alpha=0.4)

#Effects of how a customer pays on churn rate
_, axes = plt.subplots(1, 2, sharey=True, figsize=(10, 4)) 
sns.countplot(x='Symptom_1', hue='Disease',
              data=dataset_3, ax=axes[0]);
sns.countplot(x='Symptom_7', hue='Disease',
              data=dataset_3, ax=axes[1]);

#Normalising/standardising data 
scaler = StandardScaler()
scaler.fit(dataset_3.drop('Disease',axis=1))
sc_transform = scaler.transform(dataset_3.drop('Disease',axis=1))
sc_dataset_3 = pd.DataFrame(sc_transform)

sc_dataset_3.head()

#selecting independent values or columns
feature_cols = ['Disease']
X = dataset_3.iloc[:,[2,3]].values
y = dataset_3.iloc[:,4].values

#Test/Split data 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state= 42)

#feature scaling
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

#Fitting model into descision tree
classifier = DecisionTreeClassifier()
classifier = classifier.fit(X_train,y_train)

#model prediction results
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min()-1, stop= X_set[:,0].max()+1, step = 0.01),np.arange(start = X_set[:,1].min()-1, stop= X_set[:,1].max()+1, step = 0.02))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha=0.75, cmap = ListedColormap(('yellow','blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1], c = ListedColormap(('yellow','blue'))(i),label = j)
plt.title("Decision Tree(Test set)")
plt.xlabel("Disease")
plt.ylabel("Symptom_1")
plt.show()

#checking accuracy as well as other predictions

#prediction based on test data
y_pred = classifier.predict(X_test)

#Accuracy
('Accuracy Score:', metrics.accuracy_score(y_test,y_pred))

#confusion matrix of data
cm = confusion_matrix(y_test, y_pred)
cm

#Mae value
print('MAE:', metrics.mean_absolute_error(y_test, y_pred))

#mse value
print('MSE:', metrics.mean_squared_error(y_test, y_pred))

#Rmse value
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

#ReFitting model into descision tree
classifier = DecisionTreeClassifier(criterion='entropy',max_depth=100,random_state=80)
classifier = classifier.fit(X_train,y_train)

#model prediction results
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:,0].min()-1, stop= X_set[:,0].max()+1, step = 0.01),np.arange(start = X_set[:,1].min()-1, stop= X_set[:,1].max()+1, step = 0.02))
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha=0.75, cmap = ListedColormap(('yellow','blue')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set==j,0],X_set[y_set==j,1], c = ListedColormap(('yellow','blue'))(i),label = j)
plt.title("Decision Tree(Test set)")
plt.xlabel("Disease")
plt.ylabel("Symptom_1")
plt.show()

#checking accuracy as well as other predictions
#1 prediction
y_pred = classifier.predict(X_test)
#2Accuracy
('Accuracy Score:', metrics.accuracy_score(y_test,y_pred))

#confusion matrix of data
cm = confusion_matrix(y_test, y_pred)
cm

#Mae value
print('MAE:', metrics.mean_absolute_error(y_test, y_pred))

#mse value
print('MSE:', metrics.mean_squared_error(y_test, y_pred))

#Rmse value
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))



!pip install pickle5

import pickle

with open("model.pkl", 'wb') as f_out:
  pickle.dump(classifier, f_out) 
  f_out.close()

