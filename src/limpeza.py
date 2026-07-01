import pandas as pd

caminho_entrada='dados/bruto/Sample - Superstore.csv'
caminho_saida='dados/tratado/superstore_tratado.csv'

df=pd.read_csv(caminho_entrada, encoding='latin1')

print(df.head())
print(df.info())

df['Order Date']=pd.to_datetime(df['Order Date'], format='%m/%d/%Y', errors='coerce')
df['Ship Date']=pd.to_datetime(df['Ship Date'], format='%m/%d/%Y', errors='coerce')

datas_invalidas=df[df['Order Date'].isna() | df['Ship Date'].isna()]
print(f"Datas inválidas: {len(datas_invalidas)}")

datas_incoerentes=df[df['Ship Date']<df['Order Date']]
print(f"Datas incoerentes: {len(datas_incoerentes)}")
df.info()

df['dias_envio']=(df['Ship Date']-df['Order Date']).dt.days
print(df[['Order Date', 'Ship Date', 'dias_envio']].head())

df['margem_lucro']=(df['Profit']/df['Sales'])
print(df[['Sub-Category','Sales', 'Profit', 'margem_lucro']].head())

dado_nulo=df.isnull().sum()
print(f'Dados nulos por coluna: {dado_nulo}')

duplicado=df.duplicated().sum()
print(f'Linhas duplicadas: {duplicado}')