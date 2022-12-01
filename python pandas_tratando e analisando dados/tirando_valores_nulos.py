import pandas as pd
pd.set_option('display.max_column', None)

dados = pd.read_csv('../arquivos txt/aluguel_residencial.csv', sep=';')
visualizar_nulos = dados[dados['Valor'].isnull()]

a = dados.shape[0]
dados.dropna(subset=['Valor'], inplace=True)
b = dados.shape[0]
elim = a - b

dados.info()
print(elim)