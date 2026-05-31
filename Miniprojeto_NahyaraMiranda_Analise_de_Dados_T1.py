# ANÁLISE DE DADOS DE VAREJO - MINI PROJETO SCTEC

# 1 - IMPORTAR AS BIBLIOTECAS
import pandas as pd
import numpy as np

# 2 - IMPORTAR DADOS 
df = pd.read_csv("Base Varejo.csv", sep=';')

# 3 - INFORMAÇÕES INICIAIS 
print(f'Número de registros: {len(df)}')
print('\nColunas e tipo de dados:')
print(df.dtypes)



