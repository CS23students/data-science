import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
d = pd.read_csv(
    r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")
x = d.iloc[:5,-1].values.reshape(-1, 1)
y = d.iloc[:1,1].values.reshape(-1, 1)

lin = LinearRegression()
lin.fit(x, y)


y_pred = lin.predict(x)
plt.scatter(x, y)
plt.plot(x, y_pred, color='Red', label='Regression line')
plt.xlabel("BMI")
plt.ylabel("Diabetes")
plt.title("BMI vs Diabetes Outcome")
plt.show()
