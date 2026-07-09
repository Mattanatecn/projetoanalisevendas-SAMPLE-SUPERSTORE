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

df['ano']=df['Order Date'].dt.year
df['mes']=df['Order Date'].dt.month
print(df[['Order Date', 'ano', 'mes']].head())

df['margem_lucro']=(df['Profit']/df['Sales'])
print(df[['Sub-Category','Sales', 'Profit', 'margem_lucro']].head())

#A coluna Discount está em formato decimal:
coluna_discount=df['Discount']
faixas=[]
for i in coluna_discount:
    if i==0:
        classificacao='sem desconto'
    elif i>0 and i<0.2:
        classificacao='desconto baixo'
    elif i>=0.2 and i<=0.4:
        classificacao='desconto alto'
    elif i>0.4:
        classificacao='desconto agressivo'
    else:
        classificacao='verificar'
    faixas.append(classificacao)

df['faixa_desconto']=faixas
print(df[['Discount', 'faixa_desconto']].head())
print(df['faixa_desconto'].value_counts())

dado_nulo=df.isnull().sum()
print(f'Dados nulos por coluna: {dado_nulo}')

duplicado=df.duplicated().sum()
print(f'Linhas duplicadas: {duplicado}')

df.to_csv(caminho_saida, index=False, encoding='utf-8')
print(f'Arquivo tratado salvo em: {caminho_saida}')
