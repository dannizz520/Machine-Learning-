# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 12:43:48 2020

@author: Dannie
"""

""" Project 1 """

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

data=pd.read_csv(r"C:\Users\58257\Desktop\DS\python files\911.csv")

data.head()



data['zip'].value_counts().head(5)


data['twp'].value_counts().head(5)


data['title'].nunique()

     
data['Reason']=data['title'].apply(lambda title: title.split(':')[0] )

data['Reason'].value_counts()

import seaborn as sns

sns.countplot(data['Reason'])


type(data['timeStamp'].iloc[0])

data['timeStamp']=pd.to_datetime(data['timeStamp'])


data['Hour']=data['timeStamp'].apply(lambda timeStamp:timeStamp.hour )

data['Month']=data['timeStamp'].apply(lambda timeStamp:timeStamp.month )

data['Dayofweek']=data['timeStamp'].apply(lambda timeStamp: timeStamp.dayofweek)


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}



data['Dayofweek'].map(dmap)


sns.countplot(x='Dayofweek',data=data,hue='Reason')

sns.countplot(x='Month',data=data,hue='Reason')

data.groupby('Month').count().head(5)

bymonth=data.groupby('Month').count()

bymonth.info()

bymonth['twp'].plot()


sns.lmplot(x='Month',y='twp',data=bymonth.reset_index())


data['Date']=data['timeStamp'].apply(lambda timeStamp:timeStamp.date())


data.groupby('Date').count()['twp'].plot()
plt.tight_layout()

data[data['Reason']=='EMS'].groupby('Date').count()['twp'].plot()


data[data['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()


data[data['Reason']=='Fire'].groupby('Date').count()['twp'].plot()



df1=data.groupby(by=['Dayofweek','Hour']).count()['Reason'].unstack()


df1.head()

dfco=df1.corr()

sns.heatmap(dfco,annot=False)

sns.clustermap(df1)

df2=data.groupby(by=['Dayofweek','Month']).count()['Reason'].unstack()

dfco=df2.corr()

sns.heatmap(dfco)

sns.clustermap(dfco,cmap='viridis')


















