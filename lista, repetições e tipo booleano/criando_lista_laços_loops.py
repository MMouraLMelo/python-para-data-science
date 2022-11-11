idades = [18, 22, 15, 16, 25, 48, 34, 13, 16, 17]

def verifica_se_pode_dirigir(idades):
    if idades >= 18:
        print(f'{idades} anos de idade, TEM permissão para dirigir.')
    else:
        print(f'{idades} nos de idade, NÂO TEM permissão para dirigir.')
for idade in idades:
    verifica_se_pode_dirigir(idade)

