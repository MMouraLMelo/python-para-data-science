import pandas as pd

dataset = pd.read_csv('../arquivos txt/db.csv', sep=';', index_col=0)
coluna_valor = dataset[['Valor']]
loc = dataset.loc['Passat']
loc_df = dataset.loc[['Passat', 'DS5'], ['Ano', 'Quilometragem', 'Valor']]

print(loc_df)
