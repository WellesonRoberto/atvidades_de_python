'''Faça um programa que leia o nome do usuário e o imprima na vertical, em
forma de escada, usando apenas letras maiúsculas.'''

import os
os.system("cls")


nome = input("Digite o nome do usuário: ").upper()

for i in range(len(nome)):
    print(nome[:i+1])
