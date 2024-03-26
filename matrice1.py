"""Napisati program koji generira kvadratnu matricu dimenzija 5x5.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na glavnoj dijagonali matrice.
(glavna dijagonala ide od gornjeg lijevog u donji desni kut matrice)."""

import random
r = 5
s = 5

matrica = []

for i in range(r):
    red = [0] * s
    matrica.append(red)

for i in range(r):
    for j in range(s):
        matrica [i][j] = random.randrange(1, 10)
print("Matrica 5x5")
print(matrica)
zbroj = 0
for i in range(len(matrica)):
    zbroj+= matrica[i][i]

print("Zbroj je: ", zbroj)
