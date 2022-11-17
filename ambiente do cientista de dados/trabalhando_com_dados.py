import pandas as pd
pd.set_option('display.max_rows', 300)
pd.set_option('display.max_column', 10)

dataset = pd.read_csv('../arquivos txt/db.csv', sep=';')

estat = dataset[['Quilometragem', 'Valor']].describe()



print(estat)