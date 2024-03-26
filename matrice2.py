"""Napisati program koji generira kvadratnu matricu dimenzija 7x7.
Elementi su nasumični brojevi od 1 do 9.
Zatim napisati program koji računa zbroj elemenata na rubovima matrice"""

import random
r = 7
s = 7

matrica = []

for i in range(r):
    red = [0] * s
    matrica.append(red)

for i in range(r):
    for j in range(s):
        matrica [i][j] = random.randrange(1, 10)
print("Matrica 7x7")
print(matrica)

zbroj = 0
dimenzija = len(matrica)
for i in range(dimenzija):
    zbroj += matrica[0][i]  
    zbroj += matrica[dimenzija-1][i] 
    if i != 0 and i != dimenzija - 1:
        zbroj += matrica[i][0] 
        zbroj += matrica[i][dimenzija-1]

print("Zbroj elemenata na rubovima matrice je: ", zbroj)
