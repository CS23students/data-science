import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


d = pd.read_csv(
    r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")
x = d[d["Age"] == 32]["Age"].values
y = d[d["BloodPressure"] == 50]["BloodPressure"].values
z = d[d["Glucose"] == 85]["Glucose"].values
l = [len(x), len(y), len(z)]
m = min(l)
x = x[:m]
y = y[:m]
z = z[:m]
np.random.seed(42)
xs = np.random.random(100) * 10 + 0.2
ys = np.random.random(100) * 5 + 4
zs = np.random.random(100) * 15 + 0.1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, c='red', marker='o')
ax.set_xlabel("Age")
ax.set_ylabel("Blood Pressure")
ax.set_zlabel("Glucose")


plt.show()
