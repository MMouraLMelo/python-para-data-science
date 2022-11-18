dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

valores = []
for valor in dados.values():
    valores.append(valor)

soma = 0
for valor in dados.values():
    soma += valor

print(soma)

soma_func = sum(dados.values())

print(soma_func)