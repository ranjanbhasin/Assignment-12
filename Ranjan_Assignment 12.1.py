# -*- coding: utf-8 -*-
"""
Created on Sun Mar 25 11:01:10 2018

@author: Ranjan
"""
#pre-defined in problem
import pandas as pd
import matplotlib.pyplot as plt

url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'

titanic = pd.read_csv(url)

#capture count of males and females within datasets
m,f=titanic["sex"].value_counts()

plt.subplot(2,1,1)

#plot pie chart
plt.pie([m,f],labels=["male","female"],colors=["green","blue"],autopct='%1.1f%%')

plt.subplot(2,1,2)

#capture gender col of dataframe
s=titanic["sex"]
titanic["sex_num"]=s
       
#convert categorical data of gender coloumn into numeric
replace_nums={"sex_num":{"male":1,"female":0}}
titanic.replace(replace_nums,inplace=True)
sn=titanic["sex_num"]

#scatter plot with color differentiating by gender
plt.scatter(titanic["age"],titanic["fare"],c=sn,marker=".")
plt.show()