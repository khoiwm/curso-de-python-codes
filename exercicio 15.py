dias = int(input('por quantos dias utilizou o carro? '))
km = float(input('quantos Km rodou? '))
nd = (dias * 60)
nkm = (km*0.15)
preco = (nd + nkm)
print(f'o valor a ser pago será de R${preco}')