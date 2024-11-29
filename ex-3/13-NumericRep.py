import pandas as pd

df = pd.DataFrame({
    'name': ['Rahul', 'Erie', 'Ravi', 'Eesha', 'Vj', 'Moses'],
    'DateofBirth': ['17/05/2002', '16/02/2000', '25/09/1995', '11/05/2002', '15/09/2001', '01/01/1998'],
    'age': [18.5, 21.2, 22.5, 27, 23, 26]
})

print("Original DataFrame: ")
print(df)

# Factorize names to create numeric representation
df['name_numeric'] = pd.factorize(df['name'])[0]

print("\nNumeric representation of names: ")
print(df[['name', 'name_numeric']])



# OUTPUT :
# Original DataFrame: 
#      name DateofBirth   age
# 0   Rahul   17/05/2002  18.5
# 1    Erie   16/02/2000  21.2
# 2    Ravi   25/09/1995  22.5
# 3   Eesha   11/05/2002  27.0
# 4      Vj   15/09/2001  23.0
# 5   Moses   01/01/1998  26.0

# Numeric representation of names: 
#      name  name_numeric
# 0   Rahul             0
# 1    Erie             1
# 2    Ravi             2
# 3   Eesha             3
# 4      Vj             4
# 5   Moses             5
