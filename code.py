# First we imported out dataset using this code given below

#import pandas as pd
#dataset = pd.read_csv("Dataset.csv")

#Sumeet Wagh-12

#now this is the main code 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Dataset.csv')

Y = data.iloc[61:,1].values
R = data.iloc[61:,3].values
D = data.iloc[61:,5].values
X = data.iloc[61:,0]

plt.plot(X,Y)

