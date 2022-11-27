import pandas as pd

pd.set_option('display.max_column', None)

dados = pd.read_csv('../arquivos txt/aluguel_residencial.csv', sep=';')
selecao_ap = dados['Tipo'] == 'Apartamento'
selecao_apartamento = dados[selecao_ap].shape[0]

selecao_cs = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Casa de Condomínio') | (dados['Tipo'] == 'Casa de Vila')
selecao_casa = dados[selecao_cs].shape[0]

selecao_m = (dados['Area'] >= 60) & (dados['Area'] <= 100)
selecao_metros = dados[selecao_m].shape[0]

selecao = (dados['Quartos'] >= 4) & (dados['Valor'] < 2000)
selecao_valor = dados[selecao].shape[0]

print(f'Quantidade de apartamentos: {selecao_apartamento}')
print(f'Quantidade de casas: {selecao_casa}')
print(f'Imóveis com área entre 60 e 100 metros: {selecao_metros}')
print(f'Imóveis com pelo menos 4 quartos e aluguel menos que R$ 2.000,00: {selecao_valor}')
