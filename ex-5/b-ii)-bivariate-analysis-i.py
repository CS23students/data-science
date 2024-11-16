import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
d = pd.read_csv(
    r"C:\Users\cse\Documents\Data science\ex-5\AzureDiabdataset.csv")

x = d.iloc[:5,1].values.reshape(-1, 1)
y = d.iloc[:5,-1].values.reshape(-1, 1)
lin = LinearRegression()
plt.scatter(x, y)
lin.fit(x, y)
plt.xlabel("BMI")
plt.ylabel("Diabetes")
y_pred = lin.predict(x)
plt.plot(x, y_pred, color='red')
plt.show()
