import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def sig(x):
    return [1/1 + np.exp(-x)]


d = pd.read_csv(
    r"C:\Users\cse\Documents\Data science\ex-5\AzureDiabdataset.csv")
x = d.iloc[:5,1].values.reshape(-1, 1)
y = d.iloc[:5,-1].values.reshape(-1, 1)
y_pred = sig(x)
plt.scatter(x, y)
plt.xlabel("BMI")
plt.ylabel("Diabetes Coefficient")
sns.regplot(x=x, y=y, data=d, logistic=True, ci=None, color='red')
plt.show()
