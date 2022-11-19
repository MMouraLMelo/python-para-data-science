import pandas as pd

dataset = pd.read_csv('../arquivos txt/db.csv', sep=';', index_col=0)
#dataset.info()

select = dataset.Quilometragem.isna()
select_1 = dataset[dataset.Quilometragem.isna()]

tratamento = dataset.fillna(0, inplace=True)

print(dataset)