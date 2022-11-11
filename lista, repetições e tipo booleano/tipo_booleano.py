permissoes = []
idades = [18, 22, 15, 16, 25, 48, 34, 13, 16, 17]

def verifica_se_pode_dirigir(idades, permissoes):
    for idade in idades:
        if idade >= 18:
            permissoes.append(True)
        else:
            permissoes.append(False)
verifica_se_pode_dirigir(idades, permissoes)
for permissao in permissoes:
    if permissao == True:
        print('Tem permissão para dirigir.')
    else:
        print('Não tem permissão para dirigir')