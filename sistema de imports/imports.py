from random import randrange, seed

seed(10)
notas_matematica = []

for notas in range(8):
    notas_matematica.append(randrange(0, 11))


print(notas_matematica)



