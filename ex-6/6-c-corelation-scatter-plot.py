import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
d = pd.read_csv(r"C:\Users\cse\Documents\Data science\ex-5\diabetes.csv")

# Scatter plot of 'rain' vs 'temp'
sns.lmplot(x='Pregnancies', y='Age', data=d[:20])
plt.show()

sns.heatmap(d[:10], annot=True, cmap='coolwarm')
plt.show()
