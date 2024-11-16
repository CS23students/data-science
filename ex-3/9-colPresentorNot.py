import pandas as pd
d = {'col1': [1, 2, 3, 4, 7], 'col2': [
    4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df = pd.DataFrame(data=d)
print("Original Dataframe: ")
print(df)
if 'col1' in df.columns:
    print("\n'col1' is present in the DataFrame")
else:
    print("\n'col1' is not present in the DataFrame")

if 'col' in df.columns:
    print("'col' is present in the DataFrame")
else:
    print("'col' is not present in the DataFrame")
