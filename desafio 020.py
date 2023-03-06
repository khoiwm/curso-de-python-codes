# o mesmo professor do desafio anterior quer sortear a ordem
# de apresentação de trabalhos dos alunos.
# faça um programa que leia o nome dos quatros alunos e a mostre a ordem sorteada
from random import shuffle
n1 = str(input('nome do primeiro aluno: '))
n2 = str(input('nome do segundo aluno: '))
n3 = str(input('nome do terceiro aluno: '))
n4 = str(input('nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'a ordem de apresentação será: ')
print(lista)
