'''Faça um programa para cadastrar N pessoas.
O usuário deverá informar o valor de N nomes,
N sobrenomes e N idades, em três listas.
Um arquivo deve ser gerado.
A primeira linha deve informar quantas
pessoas estão cadastradas.
A partir da segunda linha do arquivo, deverá
conter o nome completo e a idade da pessoa.'''

import os
os.system("cls")

nomes = []
sobrenomes = []
idades = []

quantidade = int(input("Digite a quatidade de pessoas para cadastro: "))

for i in range(quantidade):
    nome = input(f"Digite o nome {i+1}: ")
    sobrenome = input(f"Digite o sobrenome {i+1}: ")
    idade = int(input(f"Digite a idade {i+1}: "))

    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)

arquivo = open("p09/cadastro.txt", "w", encoding="utf8")
arquivo.write(f"Há {str(quantidade)} de pessoas cadastradas.\n")

for i in range(quantidade):
    arquivo.write(f"Nome: {nomes[i]} {sobrenomes[i]} idade: {idades[i]}\n")

arquivo.close()
