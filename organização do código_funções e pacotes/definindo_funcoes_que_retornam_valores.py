def media(lista):
    valor = sum(lista) / len(lista)
    return (valor, len(lista))
media([100, 200, 250, 400, 500, 990, 425, 350, 150])

resultado, tamanho = media([100, 200, 250, 400, 500, 990, 425, 350, 150])

print(f'Média = {resultado} Tamanho da lista = {tamanho}')