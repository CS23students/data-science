import pandas as pd
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

print("Choice:\n1. Diabetes \n2. Pima India \n3. Exit\n")
ch = (int(input("Enter choice: ")))
if (ch == 1):
    d = pd.read_csv(
        r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")
elif (ch == 2):
    d = pd.read_csv(
        r"C:\Users\cse\Documents\Data science\ex-5\AzureDiabdataset.csv")
else:
    print("Invalid Data")
    exit()


print(d.head())
x = d.iloc[:5, 1].values.reshape(-1, 1)
y = d.iloc[:5, -1].values.reshape(-1, 1)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(xs=x, ys=y, c='red', s=50)
plt.show()
