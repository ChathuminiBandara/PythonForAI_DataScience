import pandas as pd
print(pd.__version__)

data = {'Name': ['Tom', 'Jerry', 'Mickey', 'Donald'],
        'Age': [20, 21, 22, 23]}

df = pd.DataFrame(data)
print(df)

print(df.loc[1, "Name"])

# Index method
print(df.iloc[1,1])