

#----------------#
#Questão 3
#----------------#

import json

# Carregar dados do faturamento diário a partir de um arquivo JSON
with open('faturamento.json') as file:
    dados = json.load(file)

faturamento_diario = dados['faturamento']

# Filtrando dias com faturamento
faturamento_validos = [valor for valor in faturamento_diario if valor > 0]

# Cálculo do menor e maior faturamento
menor_faturamento = min(faturamento_validos)
maior_faturamento = max(faturamento_validos)

# Cálculo da média mensal
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

# Contando dias com faturamento acima da média
dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

# Resultados
print(f'Menor faturamento: {menor_faturamento}')
print(f'Maior faturamento: {maior_faturamento}')
print(f'Dias com faturamento acima da média: {dias_acima_media}')
