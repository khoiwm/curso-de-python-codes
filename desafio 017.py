from math import hypot
opst = float(input('me diga o valor do cateto oposto: '))
adj = float(input('me diga o valor do cateto adjacente: '))
hipo = hypot(opst, adj)
print(f'o valor da hipotenusa é {hipo:.2f}')
