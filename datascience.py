# Data Science is about ,data gathering, finding patterns , analysis and decision-making.
# Data can be categorized into two groups:
# Structured data
# Unstructured data
# How to Structure Data?
Array = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
print(Array)
# A data frame is a structured representation of data.
import pandas as pd
data={
    "cols1":[1,2,3,4,5],
    "cols2":[6,7,8,9,10],
    "cols3":[3,4,5,6,7]
}
df=pd.DataFrame(data)
print(df)
print(df.size)
print(df.shape)
print(df.shape[0]) #no of rows
print(df.shape[1]) #no of coloumns
print()
maximum=max(1,2,3,4,5,6,7)
print(maximum)
minimum=min(1,2,3,4,5,6)
print(minimum)

import numpy as np
data=[1,2,3,4,5]
data1=np.mean(data)
print(data1)

# first extarct the data from pandas then analyze
import pandas as pd
data=pd.read_csv("data.csv",header=0,sep=",") #header are in 0th row
print(data)
# csv file=comma seperated file

# to see top 5 heading rows
print(data.head())

# next step is to clean the data,remove NaN, wrongly typed/ unregistered data
# remove blank rows
data.dropna(axis=0,inplace=True)
print(data) #remove NaN of all rows
# Data can be split into two main categories:

# Quantitative Data - Can be expressed as a number or can be quantified. Can be divided into two sub-categories:
# Discrete data: Numbers are counted as "whole", e.g. number of students in a class, number of goals in a soccer game
# Continuous data: Numbers can be of infinite precision. e.g. weight of a person, shoe size, temperature
# Qualitative Data - Cannot be expressed as a number and cannot be quantified. Can be divided into two sub-categories:
# Nominal data: Example: gender, hair color, ethnicity
# Ordinal data: Example: school grades (A, B, C), economic status (low, middle, high)
# By knowing the type of your data, you will be able to know what technique to use when analyzing them.

# to list all it's datatypes of our dataset
print(data.info())
# to change the datatypes
data["Duration"]=data["Duration"].astype(int)
print(data.info())
# to summarize the data
print(data.describe())
# count:- count no of observation