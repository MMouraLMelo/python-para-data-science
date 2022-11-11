def verifica_se_pode_dirigir():
    idade = input('Digite sua idade: ')
    idade = int(idade)
    if idade >= 18:
        print('Tem permissão para dirigir.')
    else:
        print('Não tem permissão para dirigir.')

verifica_se_pode_dirigir()