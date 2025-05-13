# describle() summary?
import pandas as pd
data=pd.read_csv("data2.csv",header=0,sep=",")
print(data.describe())
# Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.

# find 10% of percentile of max_pulse
import pandas as pd
import numpy as np
data3=pd.read_csv("data3.csv",header=0,sep=",")
pulse=data3["Max_Pulse"]
percentile10=np.percentile(pulse,10)
print(percentile10)

# Standard deviation is a number that describes how spread out the observations are.
# Standard deviation is a measure of uncertainty.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.
import numpy as np
std=np.std(data3)
print(std)
# The coefficient of variation is used to get an idea of how large the standard deviation is.
# coefficient_of_variation=std_deviation/mean
print()
import numpy as np
cv=np.std(data3)/np.mean(data3)
print(cv)

# Variance is another number that indicates how spread out the values are.
# std deviation=sqrt(variance)
# steps  to calculate variance
# 1)find mean
# 2)Find the difference from the mean for each value:
# 3)Find the square value for each difference:
# 4). Sum the squared values and find the average:
import numpy as np
variance=np.var(data3)
print("variance:",variance)
# Correlation measures the relationship between two variables.
# a function has a purpose to predict a value, by converting input (x) to output (f(x)). We can say also say that a function uses the relationship between two variables for prediction.
# The correlation coefficient measures the relationship between two variables.
# 1 = there is a perfect linear relationship between the variables (like Average_Pulse against Calorie_Burnage)
# 0 = there is no linear relationship between the variables
# -1 = there is a perfect negative linear relationship between the variables (e.g. Less hours worked, leads to higher calorie burnage during a training session)

# 1)linear relation ship (correlation coefficient=1)
import matplotlib.pyplot as plt
data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='scatter')
data3.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='scatter')
plt.show()
# 2)negative linear relation ship (correlation coefficient=-1)
import matplotlib.pyplot as plt
negative_corr = {'Hours_Work_Before_Training': [10,9,8,7,6,5,4,3,2,1],
'Calorie_Burnage': [220,240,260,280,300,320,340,360,380,400]}
negative_corr=pd.DataFrame(data=negative_corr)
negative_corr.plot(x ='Hours_Work_Before_Training', y='Calorie_Burnage', kind='scatter')
plt.show()
# 2)no linear relation ship (correlation coefficient=0)
import matplotlib.pyplot as plt
data3.plot(x ='Duration', y='Max_Pulse', kind='scatter')
plt.show()

# A correlation matrix is simply a table showing the correlation coefficients between variables.
# correlation martrix
corr_matrix=round(data3.corr(),2)
print(corr_matrix)

# We can use a Heatmap to Visualize the Correlation Between Variables:
# The closer the correlation coefficient is to 1, the greener the squares get.
# The closer the correlation coefficient is to -1, the browner the squares get.
# We can use the Seaborn library to create a correlation heat map (Seaborn is a visualization library based on matplotlib):
import matplotlib.pyplot as plt
import seaborn as sns
correlation=data3.corr()
axis_corr=sns.heatmap(correlation,vmin=-1,vmax=1,center=0,cmap=sns.diverging_palette(50,500,n=500),square=True)
print(axis_corr)
plt.show()

# Correlation measures the numerical relationship between two variables.

# A high correlation coefficient (close to 1), does not mean that we can for sure conclude an actual relationship between two variables.
# A classic example:
# During the summer, the sale of ice cream at a beach increases
# Simultaneously, drowning accidents also increase as well
# beach example
import pandas as pd
import matplotlib.pyplot as plt
Drowning_Accident = [20,40,60,80,100,120,140,160,180,200]
Ice_Cream_Sale = [20,40,60,80,100,120,140,160,180,200]
Drowning = {"Drowning_Accident": [20,40,60,80,100,120,140,160,180,200],
"Ice_Cream_Sale": [20,40,60,80,100,120,140,160,180,200]}
Drowning = pd.DataFrame(data=Drowning)
Drowning.plot(x="Ice_Cream_Sale", y="Drowning_Accident", kind="scatter")
plt.show()
correlation_beach = Drowning.corr()
print(correlation_beach)

# Correlation is a number that measures how closely the data are related
# Causality is the conclusion that x causes y.
