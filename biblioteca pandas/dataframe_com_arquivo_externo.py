import pandas as pd
pd.set_option('display.max_column', None)

dataset = pd.read_csv('../arquivos txt/db.csv', sep=';', index_col=0)

print(dataset)