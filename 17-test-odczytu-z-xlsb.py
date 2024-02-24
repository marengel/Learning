import pandas as pd

df = pd.read_excel('zalecenia.xlsx')

print(df.iloc[1, 1])
print(df.iloc[2, 1])

df.iloc[1, 1] = 50

df.to_excel('zalecenia.xlsx')
df = pd.read_excel('zalecenia.xlsx')

print(df.iloc[1, 1])
print(df.iloc[2, 1])
