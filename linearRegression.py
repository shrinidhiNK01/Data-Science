# The term regression is used when you try to find the relationship between variables.
# In Machine Learning and in statistical modeling, that relationship is used to predict the outcome of events.
# Linear regression uses the least square method.
# The concept is to draw a line through all the plotted data points. The line is positioned in a way that it minimizes the distance to all of the data points.
# The distance is called "residuals" or "errors".
# Linear Regression Using One Explanatory Variable\
# In this example, we will try to predict Calorie_Burnage with Average_Pulse using Linear Regression:
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
data4=pd.read_csv("data4.csv",header=0,sep=",")
x=data4["Average_Pulse"]
y=data4["Calorie_Burnage"]
slope,intercept,r,p,std_err=stats.linregress(x,y)
def myFunc(x):
    return slope*x+intercept
model=list(map(myFunc,x))
plt.scatter(x,y)
plt.plot(x,slope*x+intercept)
plt.ylim(ymin=0,ymax=2000)
plt.xlim(xmin=0,xmax=200)
plt.xlabel("Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.show()

# The output from linear regression can be summarized in a regression table.
# The content of the table includes:
# Information about the model
# Coefficients of the linear regression function
# Regression statistics
# Statistics of the coefficients from the linear regression function
# Other information that we will not cover in this module
import statsmodels.formula.api as smf
model=smf.ols("Calorie_Burnage ~ Average_Pulse",data=data4) #explanatory variable must be written first in the parenthesis ,OLS is short for Ordinary Least Squares
results=model.fit() #This holds a lot of information about the regression model.
print(results)
print(results.summary())

# The "Coefficients Part" in Regression Table
# Coef is short for coefficient. It is the output of the linear regression function.
# The linear regression function can be rewritten mathematically as:
# Calorie_Burnage = 0.3296 * Average_Pulse + 346.8662
#  intercept is used to adjust the model's precision of predicting!
# What is Calorie_Burnage if Average_Pulse is: 120, 130, 150, 180?
# Example
def Predict_Calorie_Burnage(Average_Pulse):
 return(0.3296*Average_Pulse + 346.8662)

print(Predict_Calorie_Burnage(120))
print(Predict_Calorie_Burnage(130))
print(Predict_Calorie_Burnage(150))
print(Predict_Calorie_Burnage(180))
'''we want to prove that it exists a relationship between Average_Pulse and Calorie_Burnage, using statistical tests.
There are four components that explains the statistics of the coefficients:
std err stands for Standard Error
t is the "t-value" of the coefficients
P>|t| is called the "P-value"
 [0.025  0.975] represents the confidence interval of the coefficients'''
# The P-value is a statistical number to conclude if there is a relationship between Average_Pulse and Calorie_Burnage.
'''We test if the true value of the coefficient is equal to zero (no relationship). The statistical test for this is called Hypothesis testing.

A low P-value (< 0.05) means that the coefficient is likely not to equal zero.
A high P-value (> 0.05) means that we cannot conclude that the explanatory variable affects the dependent variable (here: if Average_Pulse affects Calorie_Burnage).
A high P-value is also called an insignificant P-value.
'''
# Hypothesis testing is a statistical procedure to test if your results are valid.
'''Hypothesis test has two statements. The null hypothesis and the alternative hypothesis.

The null hypothesis can be shortly written as H0
The alternative hypothesis can be shortly written as HA
Mathematically written:

H0: Average_Pulse = 0
HA: Average_Pulse ≠ 0
H0: Intercept = 0
HA: Intercept ≠ 0'''
# If we reject the null hypothesis, we conclude that it exist a relationship between Average_Pulse and Calorie_Burnage. The P-value is used for this conclusion.
# A common threshold of the P-value is 0.05.
#  A P-value of 0.05 means that 5% of the times, we will falsely reject the null hypothesis. It means that we accept that 5% of the times, we might falsely have concluded a relationship.If the P-value is lower than 0.05, we can reject the null hypothesis and conclude that it exist a relationship between the variables.

# R-Squared and Adjusted R-Squared describes how well the linear regression model fits the data points:
# The value of R-Squared is always between 0 to 1 (0% to 100%).

# A high R-Squared value means that many data points are close to the linear regression function line.
# A low R-Squared value means that the linear regression function line does not fit the data well.
# Our regression model shows a R-Squared value of zero, which means that the linear regression function line does not fit the data well.
import pandas as pd
from scipy import stats
data4=pd.read_csv("data4.csv",header=0,sep=",")
x=data4["Duration"]
y=data4["Calorie_Burnage"]
slope,intercept,r,p,std_srr=stats.linregress(x,y)
def myFunc(x):
   return slope*x+intercept
model=list(map(myFunc,x))
print(model)
plt.scatter(x,y)
plt.plot(x,model)
plt.xlim(xmin=0,xmax=200)
plt.ylim(ymin=0,ymax=2000)
plt.xlabel("Duration")
plt.ylabel("Calorie_Burnage")
plt.show()

'''Coefficient of 0.3296, which means that Average_Pulse has a very small effect on Calorie_Burnage.
High P-value (0.824), which means that we cannot conclude a relationship between Average_Pulse and Calorie_Burnage.
R-Squared value of 0, which means that the linear regression function line does not fit the data well.'''

# Create a Linear Regression Table with Average_Pulse and Duration as Explanatory Variables
model=smf.ols("Calorie_Burnage~Average_Pulse+Duration",data=data4)
results=model.fit()
print(results.summary())
# The linear regression function can be rewritten mathematically as:
# Calorie_Burnage = Average_Pulse * 3.17 + Duration * 5.84 - 334.52
# Define the linear regression function in Python to perform predictions.
def Predict_Calorie_Burnage(Average_Pulse, Duration):
 return(3.1695*Average_Pulse + 5.8434 * Duration - 334.5194)

print(Predict_Calorie_Burnage(110,60))
print(Predict_Calorie_Burnage(140,45))
print(Predict_Calorie_Burnage(175,20))
'''Look at the P-value for each coefficient.

P-value is 0.00 for Average_Pulse, Duration and the Intercept.
The P-value is statistically significant for all of the variables, as it is less than 0.05.
So here we can conclude that Average_Pulse and Duration has a relationship with Calorie_Burnage.'''
# A high R-Squared value means that many data points are close to the linear regression function line.
# A low R-Squared value means that the linear regression function line does not fit the data well.
# Conclusion: The model fits the data point well!