import numpy as np

anos = np.loadtxt(fname='../arquivos txt/carros-anos.txt', dtype=int)
km = np.loadtxt(fname='../arquivos txt/carros-km.txt')
valor = np.loadtxt(fname='../arquivos txt/carros-valor.txt')

dataset = np.column_stack((anos, km, valor))

medias_colunas = np.mean(dataset, axis=0)
desvio_padrao = np.std(dataset, axis=0)
somatorio = np.sum(dataset, axis=0)

print(somatorio)