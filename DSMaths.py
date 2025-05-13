# maths helps in predictions and interpreting
# mathamatical function relate one variable to another variable
# here y=f(x)=ax+b, y=dependent,output , x=independent,input
# a=slope , coefficient of independent variable, rate of change of dependent variables
# b=intercept
# mathematical formulas gives relationship b/w those dependent variablea, and independent variables
# exploitory variable= the variable we use for prediction
# to predict calorie_burnage , formula==>f(x)=2x+80
# plot the data
import matplotlib.pyplot as plt
import pandas as pd
data2=pd.read_csv("data2.csv",header=0,sep=",")
# 2d hexagonal plot
data2.plot(x="Average_Pulse",y="Calorie_Burnage",kind="line")
plt.xlim(xmin=0)
plt.ylim(ymin=0)

plt.show()
# if the graph shows linear line, it means there is proportionality b/w them we can use average_path to predict calorie_burnage
# slope is defined as f(x2)-f(x1)/x2-x1
# find the slope
def slope(y2,y1,x2,x1):
    return (y2-y1)/(x2-x1)
print(slope(240,200,90,80))

# intercept is used to fine tune the functions ability to predict
# intercept increases the precision of prediction
# find the slope and intercept
import numpy as np
import pandas as pd
data2=pd.read_csv("data2.csv",header=0,sep=",")
x=data2["Average_Pulse"]
y=data2["Calorie_Burnage"]
slope_intercept=np.polyfit(x,y,1)
print(slope_intercept)
# 1 is the degree of function
# here we got 2 as slope and 80 as intercept
# f(x)=2x+80, according to the linear formula, f(x)=ax+b
# Now, we want to predict calorie burnage if average pulse is 135.
def myFunc(x):
    return 2*x+80
print(myFunc(135))

# plot a graph Max value of the y-axis is now 400 and for x-axis is 150:
import matplotlib.pyplot as plt
data2.plot(x="Average_Pulse", y="Calorie_Burnage", kind="line")
plt.xlim(xmin=0,xmax=150)
plt.ylim(ymin=0,ymax=400)
plt.show() 