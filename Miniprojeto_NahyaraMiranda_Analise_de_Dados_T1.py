# ANÁLISE DE DADOS DE VAREJO - MINI PROJETO SCTEC

# 1 - IMPORTAR AS BIBLIOTECAS
import pandas as pd
import numpy as np

# 2 - IMPORTAR DADOS 
df = pd.read_csv("Base Varejo.csv", sep=';')

# SPRINT 1 - VISÃO INICIAL DOS DADOS
# 3 - INFORMAÇÕES INICIAIS 
print(f'Número de registros: {len(df)}')
print('\nColunas e tipo de dados:')
print(df.dtypes)
print("")

# SPRINT 2 - TRANSFORMAÇÃO DE TIPOS

# 4 - REMOVE COLUNAS VAZIAS (Unnamed)
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col])

# 5 - CONVERTE DATA DE STR PARA DATETIME
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')

# 6 - PADRONIZA STRINGS: REMOVE ESPAÇOS EXTRAS E DEIXA MAIÚSCULO
df['CL_GENERO'] = df['CL_GENERO'].str.strip().str.upper()
df['CL_SEG'] = df['CL_SEG'].str.strip().str.upper()
df['PR_CAT'] = df['PR_CAT'].str.strip().str.upper()
df['PR_NOME'] = df['PR_NOME'].str.strip().str.upper()

# SPRINT 3 - LIMPEZA DE NULOS E DUPLICATAS

# 6 - VERIFICAÇÃO DE NULOS
print('Nulos por coluna:')
print(df.isnull().sum())

# 7 - VERIFICAÇÃO E REMOÇÃO DE DUPLICATAS
print(f'\nDuplicatas encontradas: {df.duplicated().sum()}')
df = df.drop_duplicates()
print(f'Duplicatas após limpeza: {df.duplicated().sum()}')
print(f'Registros restantes: {len(df)}')
print('')

# Tratamento de categorias inválidas (PR_CAT)
df['PR_CAT'] = df['PR_CAT'].apply(lambda x: 'Sem Categoria' if x == '#N/D' else x)
print('\nCategorias após tratamento:')
print(df['PR_CAT'].value_counts())

# Verificação do identificador de compra (CO_ID)
print(f'\nTotal de compras únicas (CO_ID): {df["CO_ID"].nunique()}')
print(f'Média de itens por compra: {len(df) / df["CO_ID"].nunique():.2f}')

# SPRINT 4 - ESTATÍSTICAS DESCRITIVAS - NÚMERO DE FILHOS 

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

# SPRINT 5: AGRUPAMENTOS

# 8 - AGRUPAMENTO 1: COMPRAS POR GÊNERO
print('=== Compras por Gênero ===')
print(df.groupby('CL_GENERO')['CO_ID'].count().sort_values(ascending=False))

# 9 - AGRUPAMENTO 2: COMPRAS POR CATEGORIA DE PRODUTO
print('\n=== Compras por Categoria de Produto ===')
print(df.groupby('PR_CAT')['CO_ID'].count().sort_values(ascending=False))

# 10 - AGRUPAMENTO 3: COMPRAS POR CLASSE ECONÔMICA
print('=== Compras por Classe Econômica ===')
print(df.groupby('CL_SEG')['CO_ID'].count().sort_values(ascending=False))

# 11 - AGRUPAMENTO 4: COMPRAS POR ESTADO CIVIL
print('\n=== Compras por Estado Civil ===')
print(df.groupby('CL_EC')['CO_ID'].count().sort_values(ascending=False))

# SPRINT 6: CONCLUSÕES

print("""
======================= CONCLUSÕES DA ANÁLISE ==============================

1. BASE DE DADOS: 830.000 registros brutos, reduzidos a 733.447 após remoção
   de 96.553 duplicatas (~11.6% da base).

2. QUALIDADE DOS DADOS: Nenhum valor nulo encontrado nas colunas principais.
   Porém, a categoria PR_CAT contém 3.228 registros com valor '#N/D',
   indicando produtos sem categoria definida.

3. PERFIL DE FILHOS: A maioria dos clientes não tem filhos (moda = 0,
   mediana = 0). A média de 1.15 sugere que uma parcela menor puxa
   a média para cima, com máximo de 4 filhos.

4. GÊNERO: Clientes do sexo feminino realizaram mais compras (382.427)
   do que masculino (351.020), uma diferença de ~8%.

5. CATEGORIAS: Alimentos lidera com folga (384.197 compras), seguido de
   Higiene e Limpeza. Bebidas e Pet aparecem com volumes menores.

6. CLASSE ECONÔMICA: Classe B concentra a maior parte das compras (468.505),
   seguida de C (205.265) e A (59.677). O público de menor renda representa
   mais volume que o de maior renda.

7. ESTADO CIVIL: Separados (3) lideram em compras (189.048), seguidos de
   Solteiros (4) e Divorciados (2). Viúvos (5) têm o menor volume (20.900).

8. PROBLEMAS REMANESCENTES: Registros '#N/D' em PR_CAT foram substituídos
   por 'Sem Categoria' (3.228 registros). A base possui 18.471 compras únicas
   com média de aproximadamente 40 itens por nota, comportamento esperado para varejo.

""")



