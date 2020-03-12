import pandas as pd
import numpy as np

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5,4), index="A B C D E".split(), columns="W X Y Z".split())

print(df)

print(df.W)

df['new'] = df["W"] + df["X"]

print(df)

df.drop('new', axis=1, inplace=True)

print(df)

print(df.loc[["A", 'B'], ['X', 'Y', 'Z']])

print(df.iloc[1:4, 2:])

bol = df >0
print(df[bol])

print(df[df["W"]>0])

print(df[df["W"]>0]["Y"]) #Retornando os valores da coluna Y levando em consideração todos os valores maiores que 0 na coluna W

print(df[(df["W"]>0) | (df["Y"]>1)])

print(df.reset_index())

#Implace=True ; o que for executado vai ser alterado no df inicial
#Ex: df.reset_index(inplace=True) reseta os indexs ta tabela df pra (0, 1, 2, 3, 4)

print(df)

#adicionando coluna com valores específicos
col = "PE BA AM RN RJ".split()
df['Estado'] = col
print(df)

print(df.set_index('Estado'))


outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(hier_index)

df = pd.DataFrame(np.random.randn(6,2), index=hier_index, columns=['A', 'B']) #criando uma tabela de multiníveis
df.index.names = ["Grupo", "Número"]

print(df)

print(df.xs("G1"))

print(df.xs(1, level="Número"))
