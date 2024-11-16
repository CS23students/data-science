import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
d = pd.read_csv(
    r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")
print(d.head())
a = input("Enter column name for x-axis: ")
b = input("Enter column name for y-axis: ")
x1 = np.linspace(d[a].min(), d[a].max(), 50)
y1 = np.linspace(d[b].min(), d[b].max(), 50)
x, y = np.meshgrid(x1, y1)
z = np.sin(x)**10+np.cos(10+y*x)*np.cos(x)
plt.xlabel(a)
plt.ylabel(b)
plt.title("Counter plot")
plt.contour(x, y, z)
plt.show()
