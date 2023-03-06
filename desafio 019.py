# um professor quer sortear um dos seus quatro alunos para apagar o quadro
# faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido
from random import choice
n1 = str(input('primeiro estudante: '))
n2 = str(input('segundo estudante: '))
n3 = str(input('terceiro estudante: '))
n4 = str(input('quarto estudante: '))
lista = [n1, n2, n3, n4]
print(f'o escolhido será {choice(lista)}')
