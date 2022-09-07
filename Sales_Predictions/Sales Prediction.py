# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 15:04:03 2021

@author: ADESH
"""

#lets import the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#lets load the required data as given test and train
train = pd.read_csv("C:\\Users\\ADESH\\Desktop\\task an\\TRAIN.csv")
test = pd.read_csv("C:\\Users\\ADESH\\Desktop\\task an\\TEST_FINAL.csv")

#Lets check for the Null value if any
train.isna().sum()
test.isna().sum()
#there is no Null values

#lets describe the data 
train.info()
test.info()

train.describe()
test.describe()

train.head()
test.head()

#Data Preprocessing
#as we have some character data we need to convert this to integer 
#so lets do labelencoding
from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()

train['Store_Type'] = lb.fit_transform(train['Store_Type'])
train['Location_Type'] = lb.fit_transform(train['Location_Type'])
train['Discount'] = lb.fit_transform(train['Discount'])
train['Region_Code'] = lb.fit_transform(train['Region_Code'])

test['Store_Type'] = lb.fit_transform(test['Store_Type'])
test['Location_Type'] = lb.fit_transform(test['Location_Type'])
test['Discount'] = lb.fit_transform(test['Discount'])
test['Region_Code'] = lb.fit_transform(test['Region_Code'])

#lets check for the sales greater than 0
train1 = train.loc[train.Sales > 0]
train1

'''
#Data lets check the unique values
df=pd.DataFrame(test)
df.Store_id.nunique()
'''

#lets create a dataset
#the store open means holiday = 1 and closed means holiday=0

test.loc[test.Holiday.isnull(), 'Holiday' ] = 1

#lets choose columns which will help to predict the sales
test.columns
columns = ['ID', 'Store_id', 'Date','Holiday', 'Discount']
#lets combine the columns and sales
madhasti = train1.groupby( columns )['Sales'].median()
madhasti

#now here we get the day wise sales
madhasti = madhasti.reset_index()
madhasti

#now lets add the madhasti on the test dataset on the left or right side
test1 = pd.merge(test, madhasti, on = columns, how='right')

#Now lets compare the length of test1 and test


test1.loc[ test1.Holiday == 0, 'Sales' ] = 0
test1.loc[ test1.Holiday == 0]

assert( test1.Sales.isnull().sum() == 0 )


#Lets save the final file
import os
os.
test1[[ 'ID', 'Sales' ]].to_csv("sample_submission.csv", index = False )

submission = pd.read_csv("sample_submission.csv")
