import pandas as pd
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
print("Press 1 for UCI diabetes dataset and 2 for Pima Indian diabetes dataset")
ch = int(input("Enter choice: "))
if ch == 1:
    d = pd.read_csv(r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")
else:
    d = pd.read_csv(
        r"C:\Users\cse\Documents\Data science\ex-5\AzureDiabdataset.csv")
print("Top rows: \n", d.head())
print("Bottom rows: \n", d.tail())
a = input("Enter column name to find mean: ")
print("Mean of ", a, "is: ", d[a].mean())
b = input("Enter column name to find mean: ")
print("Media of ", b, "is: \n", d[b].median())
c = input("Enter column name to find mode: ")
print("Mode of ", c, "is: \n", d[c].mode())
g = input("Enter column name to find frequency: ")
print("Frequency of ", g, "is: \n", d[g].value_counts()[0:4])
e = input("Enter column name to find variance: ")
print("Frequency of ", g, "is:\n", d[e].var())
f = input("Enter column name to find standard deviation: ")
print("Standard Deviation of ", f, "is:\n", d[f].std())
h = input("Enter column name to find skewnes: ")
print("Skewness value: ", skew(d[h], axis=0, bias=True))
i = input('Enter column name to find kurtosis: ')
print("Kurtosis value: ", kurtosis(d[i], axis=0, bias=True))
