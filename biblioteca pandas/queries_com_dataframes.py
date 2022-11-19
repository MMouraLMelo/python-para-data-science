import pandas as pd

dataset = pd.read_csv('../arquivos txt/db.csv', sep=';', index_col=0)
select = dataset.Motor == 'Motor Diesel'
select_1 = dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)]
select_2 = dataset.query('Motor == "Motor Diesel" and Zero_km == True')

print(select_2)