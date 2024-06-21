"""Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva manjih od prosljeđenog parametra.
"""


def parni(a):
    for i in range(0, a):
        if i%2 ==0:
            yield i

def neparni(a):
    for i in range(0, a):
        if i%2 !=0:
            yield i


parni = list(parni(100))
neparni = list(neparni(100))
print(f"\nParni brojevi su {parni} \nNeparni su {neparni}")
