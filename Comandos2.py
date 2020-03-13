import pandas as pd
import numpy as np

d = {'a':[1,2,np.nan], 'b':[5, np.nan, np.nan], 'c':[1,2,3]}

print(d)

df = pd.DataFrame(d)

print(df)
print("\n")
print(df.dropna()) #por valor padrão, exclui linhas inteiras que possuem valores vazios
print("\n")
print(df.dropna(thresh=2)) #só vai excluir linhas que possuem 2 valores faltantes
print("\n")
print(df.fillna(value = "10")) #substitui os valores vazios por algum valor que sera passado
print("\n")
print(df["a"].fillna(value=df["a"].mean())) #substitui o valor faltante pela media dos valores que aquela coluna possui (no caso da coluna A = 1.5)
print("\n")
print(df.fillna(method='ffill')) #foward fill  = preenche os valores faltantes pelos valores dos métodos anteriores

