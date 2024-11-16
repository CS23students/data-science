import pandas as pd
import matplotlib.pyplot as plt
d = pd.read_csv(
    r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")
print(d.head())
a = input("Enter the column name to form density plot: ")
d[a].plot.density(color='blue')
plt.title("Density Plot")
plt.xlabel(a)
plt.show()
