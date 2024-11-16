import pandas as pd

d = {'col1': [1, 2, 3, 4], 'col2': [4, 5, 6, 7], 'col3': [8, 9, 10, 11]}
df = pd.DataFrame(data=d)
print("Original Dataframe: ", df)
print("Number of columns: ", len(df.columns))
