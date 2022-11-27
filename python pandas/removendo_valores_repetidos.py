import pandas as pd

dados = pd.read_csv('../arquivos txt/aluguel.csv', sep=';')
tipo_de_imovel = dados['Tipo']

dupli = tipo_de_imovel.drop_duplicates()

print(dupli)