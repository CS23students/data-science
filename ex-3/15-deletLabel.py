import pandas as pd
details = {
    'name': ['Abi', 'Arun', 'Anu', 'Durai', 'Balu'],
    'age': [23, 20, 18, 21, 29],
    'university': ['ABC', 'DIR', 'AI', 'AJ', 'XYX']
}

df = pd.DataFrame(details, columns=['name', 'age', 'university'], index=[
                  'a', 'b', 'c', 'd', 'e'])

update = df.drop(['b', 'c'])
print(update)
