import re
import json
import datetime

# Função para verificar se um valor é numérico
def is_numeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

# Função para verificar se um valor é uma data
def is_date(val):
    try:
        datetime.datetime.strptime(val, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Função para converter um valor para o tipo apropriado
def convert_value(val):
    if is_numeric(val):
        return float(val)
    elif is_date(val):
        return val
    else:
        return val

# Lendo o arquivo SQL
with open('GeneroTipo.sql', 'r') as f:
    sql = f.read()

# Encontrando todas as instruções INSERT
inserts = re.findall(r"INSERT INTO tabela \((.*?)\) VALUES \((.*?)\);", sql)

# Criando uma lista para armazenar os dados em formato JSON
dados_json = []

# Para cada instrução INSERT
for colunas, valores in inserts:
    # Dividindo as colunas e os valores pelas vírgulas
    colunas = colunas.split(', ')
    valores = valores.split(', ')

    # Removendo as aspas dos valores e convertendo para o tipo apropriado
    valores = [convert_value(valor.strip("'")) for valor in valores]

    # Criando um dicionário para armazenar os dados da linha
    linha_json = {coluna: valor for coluna, valor in zip(colunas, valores)}

    # Adicionando o dicionário na lista
    dados_json.append(linha_json)

# Convertendo a lista em uma string JSON
json_str = json.dumps(dados_json, indent=4)

# Salvando a string JSON em um arquivo
with open('GeneroTipo.json', 'w') as f:
    f.write(json_str)
