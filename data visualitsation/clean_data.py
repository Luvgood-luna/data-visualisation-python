import pandas as pd

df = pd.read_csv('/home/craver/Downloads/data_breach.csv')
name = df['Entity']
records = df['Records']

df = df[(df['Records'] != 'unknown') & (df['Records'].notna())]

df['Records'] = pd.to_numeric(df['Records'], errors='coerce')

df = df[(df['Entity'] != 'Unknown')]  

df = df.dropna(subset=['Records'])

top_20 = df.nlargest(20,['Records'])

ds = pd.DataFrame(columns=['Company', 'Records', 'Year', 'Organization type', 'Method' ])
ds['Company'] = top_20['Entity']
ds['Records'] = top_20['Records']
ds['Year'] = top_20['Year']
ds['Organization type'] = top_20['Organization type']
ds['Method'] = top_20['Method']

print("ok")
ds.to_csv('Top20.csv', index=False)