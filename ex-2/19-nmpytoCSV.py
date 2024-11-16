import numpy as np
import pandas as pd


data = np.array([[19, 71, 93], [5, 12, 31], [86, 76, 65]])
np.savetxt("test.csv", data, delimiter=',')
df = pd.read_csv("test.csv")
print("CSV file content:\n")
print(df)
