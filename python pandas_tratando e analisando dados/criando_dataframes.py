import pandas as pd

data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
df = pd.DataFrame(data=data)
index = ['Linha' + str(i) for i in range(3)]
columns = ['Coluna' + str(i) for i in range(4)]
df = pd.DataFrame(data=data, index=index, columns=columns)


print(df)