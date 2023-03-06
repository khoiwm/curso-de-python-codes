# faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo
import math
ang = float(input('me diga o valor de um ângulo: '))
sen = math.sin(math.radians(ang))
con = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'o SENO desse ângulo é {sen:.2f}')
print(f'o COSSENO equivale a {con:.2f}')
print(f'e a TANGENTE é {tan:.2f}')
