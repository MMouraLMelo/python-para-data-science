import pandas as pd
import row as row

dataset = pd.read_csv('../arquivos txt/db.csv', sep=';', index_col=0)
iteracao = dataset.iterrows()


for index, row in dataset.iterrows():
    if 2022 - row['Ano'] != 0:
        dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2022 - row['Ano'])
    else:
        dataset.loc[index, 'Km_media'] = 0

print(dataset)


