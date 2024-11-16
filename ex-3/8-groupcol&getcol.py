import pandas as pd
df = pd.DataFrame({
    'col1': ['c1', 'c2', 'c2', 'c2', 'c2', 'c3'],
    'col2': [1, 2, 3, 3, 4, 6]
})
print("Original DataFrame:\n", df)

grouped_df = df.groupby('col1')['col2'].apply(list).reset_index()

print("\nGrouped on 'col1':\n", grouped_df)
