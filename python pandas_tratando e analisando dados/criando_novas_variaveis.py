import pandas as pd
pd.set_option('display.max_column', None)

dados = pd.read_csv('../arquivos txt/aluguel_residencial.csv', sep=',')


print(dados)