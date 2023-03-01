estados = ['SP', 'RJ', 'MG', 'ES', 'Outros']
faturamento = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]

total_faturamento = sum(faturamento)
print(f"Valor total do faturamento: {total_faturamento}")

for i in range(len(estados)):
    estado = estados[i]
    valor = faturamento[i]
    percentual = valor / total_faturamento * 100
    print(f"{estado}: {percentual:.2f}%")