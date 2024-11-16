import pandas as pd
import numpy as np

data = {
    'name': ['Hepsi', 'Blessy', 'Ahamed', 'Durai', 'Abi', 'Max'],
    'score': [90, 50, 60, 40, np.nan, 30],
    'attempt': [1, 1, 2, 2, 3, 1],
    'quality': ['yes', 'no', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f']
df = pd.DataFrame(data, index=labels)
print(df)
