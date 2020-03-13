#Group By

import pandas as pd
import numpy as np

data = {"Empresa": ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Nome': ['Sam', 'Charlie', 'Amy', "Vanessa", 'Carl', "Sarah"],
        'Venda': [200, 120, 340, 124, 242, 350]}

df = pd.DataFrame(data)

print(df)

print('\n')
#Agrupar

grupo = df.groupby('Empresa') #Selecionando os dados de venda por empresa

print(grupo) #aqui ele vai indicar onde a variavel vai estar salva na memória

#Agora as operações serão feitas com a variável.operações

print('\n')

print(grupo.sum())

print('\n')

print(grupo.mean()) #media

print('\n')

print(grupo.describe()) #relatorio

print('\n')

print(grupo.count())

print('\n')

print(grupo.sum().loc["GOOG"])