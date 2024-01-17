import pandas as pd
import csv
import unidecode

# Função para verificar se um valor é numérico
def is_numeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

# Função para converter um valor numérico para float
def convert_to_float(val):
    if isinstance(val, str):
        val = val.replace(',', '.')
    try:
        return float(val)
    except ValueError:
        return val

# Lendo o arquivo CSV
data = pd.read_csv('Pagamento.csv', delimiter=';', encoding='utf-8')

# Convertendo os valores numéricos para float
for col in data.columns:
    data[col] = data[col].apply(convert_to_float)

# Abrindo o arquivo .sql para escrita
with open('Pagamento.sql', 'w', encoding='utf-8') as f:
    # Escrevendo os comandos SQL no arquivo
    for index, row in data.iterrows():
        colunas = ', '.join(unidecode.unidecode(key).replace(' ', '_') for key in row.keys())
        valores = ', '.join(f"'{str(i)}'" if not is_numeric(i) else str(i) for i in row)
        f.write(f"INSERT INTO tabela ({colunas}) VALUES ({valores});\n")
