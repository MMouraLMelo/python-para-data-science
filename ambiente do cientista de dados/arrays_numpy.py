import numpy as np

km = np.loadtxt('../arquivos txt/carros-km.txt')
anos = np.loadtxt('../arquivos txt/carros-anos.txt', dtype = int)

km_media = km / (2022 - anos)

print(km_media)