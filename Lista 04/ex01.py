'''Desenvolva um programa que possua dois vetores/listas (A e B) de 5
elementos cada (o usuário insere os valores nos dois vetores). Crie um
terceiro vetor (C) que seja a união entre os 2 vetores anteriores, ou seja,
que contém os números dos dois vetores. Após isso, apresente:

a) A soma dos números pares do vetor C;
b) A média dos números ímpares do vetor C;
c) O menor valor do vetor C'''

import os
os.system("cls")

lista1 = []
lista2 = []
lista3 = []
i = 0
par = []
impar = []

for i in range(5):
    lista1.append(int(input("Digite um número para lista 1: ")))

for i in range(5):
    lista2.append(int(input("Digite um número para a lista 2: ")))

print(f"Lista 1:{lista1}")
print(f"Lista 2:{lista2}")
lista3 = lista1 + lista2
print(f"Lista 3: {lista3}")
print()

for i in range(len(lista3)):
    if (lista3[i] % 2) == 0:
        par.append(lista3[i])
    else:
        impar.append(lista3[i])

print(f"Soma dos pares: {sum(par)}")
print(f"Soma dos ímpares: {sum(impar)}")
print(f"O menor número é: {min(lista3)}")
