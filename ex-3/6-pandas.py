import pandas as pd

data = {'col1': [1, 2, 3, 4, 7], 'col2': [
    4, 5, 6, 7, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data)
print("Original Dataframe:\n")
print(df)
print("\nAll cloumn except col3:\n")
df1 = df.loc[:, df.columns != 'col3']
print(df1)
