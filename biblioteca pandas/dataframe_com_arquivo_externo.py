import pandas as pd

dataset = pd.read_csv('../arquivos txt/db.csv', sep=';', index_col=0)

print(dataset)