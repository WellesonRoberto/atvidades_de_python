'''Faça um programa que peça ao usuário um número
inteiro. Em seguida mostre na tela os números de 0 a n
(número escolhido) e seus respectivos quadrados, como
na seguinte forma {n : n*n}.'''

dicionario = {}
numero = int(input("Digite um número: "))

for i in range(0, numero + 1, 1):
    dicionario[i] = i*i

print(dicionario)
