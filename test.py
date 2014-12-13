import math

Dab = math.pow(10, -10)

td1 = 0.25
td2 = 0.0025
td3 = 0.000025

lstr = input("Podaj czas: ")
czas = float(lstr)

x1 = czas / td1
x2 = czas / td2
x3 = czas / td3
print(x1, x2, x3)
suma1 = 0
suma2 = 0
suma3 = 0

for i in range(1, 50):
    suma1 = suma1 + ( 1. / math.pow(i, 2)) * math.exp(-math.pow(i * math.pi, 2) * x1)
    suma2 = suma2 + (1. / math.pow(i, 2)) * math.exp(-math.pow(i * math.pi, 2) * x2)
    suma3 = suma3 + (1. / math.pow(i, 2)) * math.exp(-math.pow(i * math.pi, 2) * x3)
    print (-math.pow(i * math.pi, 2) * x1)


print(suma2, suma1, suma3)
wynik1 = 1 - (6 / (math.pow(math.pi, 2) * suma1))
wynik2 = 1 - (6 / (math.pow(math.pi, 2) * suma2))
wynik3 = 1 - (6 / (math.pow(math.pi, 2) * suma3))

print wynik1, wynik2, wynik3