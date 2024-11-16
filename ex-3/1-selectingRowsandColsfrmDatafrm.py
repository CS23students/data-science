import pandas as pd
import numpy as np

exam_data = {
    'name': ['Davis', 'Kali', 'James', 'Imily', 'Michael', 'Kavi', 'Sree', 'Kavin', 'John'],
    'score': [12.5, 9.16, np.nan, 9.20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2],
    'quality': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'no', 'no', 'no']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

df = pd.DataFrame(exam_data, index=labels)

print(df.loc[['b', 'd', 'f', 'g'], ['name', 'quality']])
