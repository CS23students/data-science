import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import pandas as pd

d = pd.read_csv(
    r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")
ch = input("Enter the column the name to plot normal curve: ")
m = d[ch].mean()
std = d[ch].std()
print("Mean: ", m, "\n Standard Deviatoin: ", std)
a = np.arange(-15, 15, 0.01)
plt.plot(a, norm.pdf(a, m, std))
plt.show()
