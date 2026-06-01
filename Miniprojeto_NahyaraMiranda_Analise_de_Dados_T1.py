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
print("")

# TRANSFORMAÇÃO DE TIPOS

# 4 - REMOVE COLUNAS VAZIAS (Unnamed)
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col])

# 5 - CONVERTE DATA DE STR PARA DATETIME
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')

# 6 - PADRONIZA STRINGS: REMOVE ESPAÇOS EXTRAS E DEIXA MAIÚSCULO
df['CL_GENERO'] = df['CL_GENERO'].str.strip().str.upper()
df['CL_SEG'] = df['CL_SEG'].str.strip().str.upper()
df['PR_CAT'] = df['PR_CAT'].str.strip().str.upper()
df['PR_NOME'] = df['PR_NOME'].str.strip().str.upper()

print(df.dtypes)
print(df.head())



