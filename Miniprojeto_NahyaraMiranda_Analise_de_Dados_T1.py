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

# LIMPEZA DE NULOS E DUPLICATAS

# 6 - VERIFICAÇÃO DE NULOS
print('Nulos por coluna:')
print(df.isnull().sum())

# 7 - VERIFICAÇÃO E REMOÇÃO DE DUPLICATAS
print(f'\nDuplicatas encontradas: {df.duplicated().sum()}')
df = df.drop_duplicates()
print(f'Duplicatas após limpeza: {df.duplicated().sum()}')
print(f'Registros restantes: {len(df)}')
print('')

# ESTATÍSTICAS DESCRITIVAS - NÚMERO DE FILHOS 

print('=== Estatísticas Descritivas - Número de Filhos dos Clientes ===')
print(f'Contagem : {df["CL_FHL"].count()}')
print(f'Média    : {df["CL_FHL"].mean():.2f}')
print(f'Mediana  : {df["CL_FHL"].median():.2f}')
print(f'Moda     : {df["CL_FHL"].mode()[0]}')
print(f'Desvio P.: {df["CL_FHL"].std():.2f}')
print(f'Mínimo   : {df["CL_FHL"].min()}')
print(f'Máximo   : {df["CL_FHL"].max()}')
print(f'Q1 (25%) : {df["CL_FHL"].quantile(0.25)}')
print(f'Q2 (50%) : {df["CL_FHL"].quantile(0.50)}')
print(f'Q3 (75%) : {df["CL_FHL"].quantile(0.75)}')



