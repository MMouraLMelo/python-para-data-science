import pandas as pd
pd.set_option('display.max_column', None)

dados = pd.read_csv('../arquivos txt/aluguel_residencial.csv', sep=';')
selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull())

a = dados.shape[0]
dados = dados[~selecao]
b = dados.shape[0]
elim = a - b

tratando = dados.fillna({'Condominio': 0, 'IPTU': 0})
tratando.info()

dados.to_csv('../arquivos txt/aluguel_residencial.csv', sep=';', index=False)

print(selecao)


