# ANÁLISE DE DADOS DE VAREJO - MINI PROJETO SCTEC

# IMPORTAR AS BIBLIOTECAS
import pandas as pd
import numpy as np
from datetime import datetime
import csv


# SPRINT 1: IMPORTAÇÃO E VISUALIZAÇÕES INICIAIS
# IMPORTAR DADOS 
with open('Base Varejo.csv', encoding='utf-8') as f:
    leitor = csv.DictReader(f, delimiter=';')
    registros = list(leitor)

print(f'Registros lidos com csv.DictReader: {len(registros)}')
print(f'Colunas: {list(registros[0].keys())}')

# Converte para DataFrame para análise estruturada
df = pd.DataFrame(registros)

# Converte colunas numéricas
cols_int = ['CO_ID', 'CL_ID', 'CL_EC', 'CL_FHL', 'PR_ID']
df[cols_int] = df[cols_int].astype(int)

# INFORMAÇÕES INICIAIS 
print(f'Número de registros: {len(df)}')
print('\nColunas e tipo de dados:')
print(df.dtypes)
print("")

# SPRINT 2: TRANSFORMAÇÃO DE TIPOS

# Remove colunas vazias (Unnamed)
df = df.drop(columns=[col for col in df.columns if 'Unnamed' in col])
df = df.drop(columns=[''])

# Converte DATA de string para datetime
df['DATA'] = df['DATA'].apply(lambda x: datetime.strptime(x, '%d/%m/%Y'))

# Padroniza strings: remove espaços extras e coloca em maiúsculo
df['CL_GENERO'] = df['CL_GENERO'].str.strip().str.upper()
df['CL_SEG'] = df['CL_SEG'].str.strip().str.upper()
df['PR_CAT'] = df['PR_CAT'].str.strip().str.upper()
df['PR_NOME'] = df['PR_NOME'].str.strip().str.upper()

# Tipos de dados após transformações
print('\nColunas e tipos após transformações:')
print(df.dtypes)
print("")

# SPRINT 3: LIMPEZA DE NULOS E DUPLICATAS

# Verificação de nulos
print('Nulos por coluna:')
print(df.isnull().sum())

# Verificação e remoção de duplicatas
print(f'\nDuplicatas encontradas: {df.duplicated().sum()}')
df = df.drop_duplicates()
print(f'Duplicatas após limpeza: {df.duplicated().sum()}')
print(f'Registros restantes: {len(df)}')
print('')

# Tratamento de categorias inválidas (PR_CAT)
def tratar_categoria(valor):
    if valor == '#N/D':
        return 'Sem Categoria'
    else:
        return valor

df['PR_CAT'] = df['PR_CAT'].apply(tratar_categoria)
print('\nCategorias após tratamento:')
print(df['PR_CAT'].value_counts())

# Verificação do identificador de compra (CO_ID)
print(f'\nTotal de compras únicas (CO_ID): {df["CO_ID"].nunique()}')
print(f'Média de itens por compra: {len(df) / df["CO_ID"].nunique():.2f}')

# Validação de identificadores
print(f'\nCO_ID - valores únicos: {df["CO_ID"].nunique()}')
print(f'CL_ID - valores únicos: {df["CL_ID"].nunique()}')
print(f'Valores negativos em CO_ID: {(df["CO_ID"] < 0).sum()}')
print(f'Valores negativos em CL_ID: {(df["CL_ID"] < 0).sum()}')

# Validação de datas
print(f'\nData mais antiga: {df["DATA"].min().strftime("%d/%m/%Y")}')
print(f'Data mais recente: {df["DATA"].max().strftime("%d/%m/%Y")}')

# SPRINT 4: ESTATÍSTICA DESCRITIVA - NÚMERO DE FILHOS (CL_FHL)

print('\n=== Estatísticas Descritivas - Número de Filhos (CL_FHL) ===')
print(f'Contagem : {df["CL_FHL"].count()}')
print(f'Média    : {np.mean(df["CL_FHL"]):.2f}')
print(f'Mediana  : {np.median(df["CL_FHL"]):.2f}')
print(f'Moda     : {df["CL_FHL"].mode()[0]}')
print(f'Desvio P.: {np.std(df["CL_FHL"]):.2f}')
print(f'Mínimo   : {df["CL_FHL"].min()}')
print(f'Máximo   : {df["CL_FHL"].max()}')
print(f'Q1 (25%) : {df["CL_FHL"].quantile(0.25)}')
print(f'Q2 (50%) : {df["CL_FHL"].quantile(0.50)}')
print(f'Q3 (75%) : {df["CL_FHL"].quantile(0.75)}')

# SPRINT 5: AGRUPAMENTOS

# Agrupamento 1: compras por gênero
print('\n=== Compras por Gênero ===')
print(df.groupby('CL_GENERO')['CO_ID'].count().sort_values(ascending=False))

# Agrupamento 2: compras por categoria de produto
print('\n=== Compras por Categoria de Produto ===')
print(df.groupby('PR_CAT')['CO_ID'].count().sort_values(ascending=False))

# Agrupamento 3: compras por segmentação econômica
print('\n=== Compras por Classe Econômica ===')
print(df.groupby('CL_SEG')['CO_ID'].count().sort_values(ascending=False))

# Agrupamento 4: compras por estado civil
print('\n=== Compras por Estado Civil ===')
print(df.groupby('CL_EC')['CO_ID'].count().sort_values(ascending=False))

# EXPORTAR BASE LIMPA
df.to_csv('df_limpo.csv', index=False, sep=';')
print('Base limpa exportada: df_limpo.csv')

# SPRINT 6: CONCLUSÕES

print("""
========================= CONCLUSÕES DA ANÁLISE ============================

1. BASE DE DADOS: 830.000 registros brutos, reduzidos a 733.447 após remoção
   de 96.553 duplicatas (~11.6% da base).

2. QUALIDADE DOS DADOS: Nenhum valor nulo encontrado nas colunas principais.
   Porém, foram encontrados 3.228 registros com valor '#N/D' em PR_CAT,
   substituídos por 'Sem Categoria'.

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

8. IDENTIFICADORES E DATAS: 18.471 notas fiscais e 1.000 clientes únicos,
   sem valores negativos em nenhum dos identificadores. Datas cobrem o
   período de jan/2019 a dez/2022, sem inconsistências encontradas.
   Média de, aproximadamente, 40 itens por nota.

""")




