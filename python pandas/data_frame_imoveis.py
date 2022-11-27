import pandas as pd
pd.set_option('display.max_column', None)

data = pd.read_csv('../arquivos txt/aluguel.csv', sep=';')
duplicados = list(data['Tipo'].drop_duplicates())
residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']

series_boolean = data['Tipo'].isin(residencial)

dados_residencial = data[series_boolean]
volume = dados_residencial.shape[0]
index = dados_residencial.index = range(volume)


print(index)

dados_residencial.to_csv('../arquivos txt/aluguel_residencial.csv', sep=';', index=False)