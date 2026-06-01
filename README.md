# 📊 Miniprojeto Analise de Dados com Python - SCTEC  - ANALISANDO DADOS DO VAREJO


Análise exploratória de uma base de dados de varejo com 830.000 registros, desenvolvida como mini-projeto avaliativo do curso de Análise de Dados com Python - T1 no SCTEC.

---

## 🛠️ Tecnologias
- Python 3.12.1
- Pandas
- NumPy

---

## 📁 Estrutura do Repositório
```
Miniprojeto_NahyaraMiranda_Analise_de_Dados_T1/
│
├── Miniprojeto_NahyaraMiranda_Analise_de_Dados_T1.py
├── Base Varejo.csv
├── df_limpo.csv
├── requirements.txt
├── README.md
└── README_NahyaraMiranda_Analise_de_Dados_T1.md
```

---

## 📖 A História da Análise

O projeto começou com uma tarefa simples: carregar uma base de dados de varejo e entender o que ela tinha. Ao abrir o arquivo com `csv.DictReader`, já apareceu o primeiro problema — o CSV usava `;` como separador, não vírgula, e gerava colunas extras vazias (`Unnamed`) por causa de separadores no final de cada linha.

Com o DataFrame criado, a inspeção inicial revelou que a coluna `DATA` estava como string, impedindo qualquer análise temporal. A conversão para `datetime` usando o módulo `datetime` foi o primeiro passo de transformação. Em seguida, as colunas de texto foram padronizadas com `strip()` e `upper()` para evitar que variações como `" f"` e `"F"` fossem tratadas como categorias diferentes.

Na limpeza de nulos, a base surpreendeu positivamente: nenhum valor nulo nas colunas principais. Porém, ao verificar as categorias de produto, apareceram 3.228 registros com o valor `#N/D`, ou seja,  produtos vendidos sem categoria registrada. A escolha foi substituir por `"Sem Categoria"` em vez de remover, pois a venda em si aconteceu e seus dados são válidos.

O maior desafio foi decidir o que fazer com as 96.553 duplicatas (~11,6% da base). Poderíamos interpretar cada linha como um item individual de uma compra — afinal, um cliente pode comprar duas bananas e elas aparecem em duas linhas. No entanto, como a base não possui coluna de quantidade, não há como distinguir um item repetido de um registro duplicado por erro. A escolha foi tratar todos os registros idênticos como duplicatas e manter apenas uma ocorrência, assumindo que cada linha representa um item único adquirido.

A validação dos identificadores confirmou consistência: sem valores negativos em `CO_ID` ou `CL_ID`, e as datas cobrem um período coerente de janeiro de 2019 a dezembro de 2022, sem datas inválidas.

---

## 💡 Principais Insights
1. A base passou de 830.000 para 733.447 registros após remoção de ~11,6% de duplicatas
2. Clientes do sexo feminino realizaram ~8% mais compras que o masculino
3. Alimentos é a categoria mais comprada, representando mais da metade das vendas
4. A maioria dos clientes não tem filhos (moda = 0, mediana = 0)
5. A Classe B concentra o maior volume de compras (64% do total)
6. Foram identificados 3.228 registros com categoria inválida (`#N/D`), tratados como "Sem Categoria"

---

## 📖 ETL e Qualidade de Dados

**ETL** (Extract, Transform, Load) é o processo de extrair dados de uma fonte, transformá-los para um formato adequado à análise e carregá-los em um destino final. Neste projeto, cada etapa foi aplicada de forma prática:

- **Extração:** leitura da base `Base Varejo.csv` com `csv.DictReader`, identificando separador, tipos de dados e colunas irrelevantes.
- **Transformação:** conversão da coluna `DATA` para `datetime`, padronização de strings, remoção de duplicatas e tratamento de categorias inválidas.
- **Carga:** o resultado final é um DataFrame limpo, pronto para análise e geração de estatísticas.

**Qualidade de dados** é um fator crítico em qualquer análise. Dados sujos (duplicatas, tipos incorretos, valores inválidos) comprometem qualquer conclusão. Neste projeto, a base apresentou 11,6% de registros duplicados e categorias com valor `#N/D`, que foram devidamente tratados. A ausência de valores nulos nas colunas principais indica uma coleta de dados relativamente consistente.

---

## 🔍 Justificativa das Escolhas de Limpeza

- **Remoção de duplicatas:** registros 100% idênticos não agregam informação e distorcem contagens e estatísticas. Como a base não possui coluna de quantidade, não há como distinguir um item repetido de um erro de registro — a escolha foi manter apenas uma ocorrência por registro idêntico.
- **Colunas `Unnamed` e coluna vazia:** geradas pelo separador extra no final do CSV, todas sem nenhum registro válido. Removidas por não conterem informação útil.
- **Conversão de `DATA` para datetime:** a coluna estava como string, o que impede qualquer análise temporal. A conversão permite filtros por período e ordenação cronológica.
- **Padronização de strings:** evita que variações como `" f"`, `"F"` e `"f"` sejam tratadas como categorias diferentes nos agrupamentos.
- **`#N/D` substituído por `"Sem Categoria"`:** a remoção causaria perda de dados de venda válidos. A substituição preserva o registro e sinaliza o problema.

---

## ▶️ Como executar
```bash
pip install pandas numpy
python Miniprojeto_NahyaraMiranda_Analise_de_Dados_T1.py
```
> ⚠️ O arquivo `Base Varejo.csv` deve estar na mesma pasta do script.
> 
> Baixe em: [Base Varejo | Kaggle](https://www.kaggle.com/datasets/namespaiva/base-varejo)
> 
> O arquivo `df_limpo.csv` é gerado automaticamente ao executar o script.

---

## 👩‍💻 Autora
**Nahyara Miranda** — Análise de Dados com Python - T1 | SCTEC
