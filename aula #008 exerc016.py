# crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# ex: digite um número: 6.127, o número tem a parte inteira 6
import math
num = float(input('digite um número Real (ex: 6.5): '))
inteiro = math.floor(num)
print(f'o número {num} tem sua parte inteira {inteiro}')
