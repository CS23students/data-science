import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

d = pd.read_csv(
    r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")
sns.histplot(d['Age'])
plt.show()
