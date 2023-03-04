prod = float(input('qual o valor do produto que está adquirindo? R$'))
vista = (prod * 10 / 100)
parcela = (prod * 1.08)
print(f'seu produto que vale R${prod}, comprado à vista, terá um desconto de 10%, ou seja, custará {prod-vista}.\nSe for parcelado, terá um aumento de 08%, ou seja, será de {parcela}.\n')
