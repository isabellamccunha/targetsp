import json

with open('faturamento.json') as f:
    calculo_faturamento = json.load(f)

valores = [dia['valor'] for dia in calculo_faturamento if dia['valor'] > 0]

menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = len([dia for dia in valores if dia > media_mensal])

print(f'Menor faturamento: R$ {menor_faturamento:.2f}')
print(f'Maior faturamento: R$ {maior_faturamento:.2f}')
print(f'Dias acima da média: {dias_acima_da_media}')
