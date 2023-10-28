'''Desenvolva um programa no qual o usuário deverá inserir a
quantidade de pessoas que desejam realizar uma doação a um centro
de apoio no Recife. Depois, pergunte os nomes dos doadores e o
valor que deseja doar, respectivamente. No final imprima o
dicionário com o nome do doador (chave) e o valor inserido. Além
disso, exiba o total em doações arrecadado.'''

import os
os.system("cls")


qte_pessoas = int(input("Digite a quantidade de pessoas que vão doar:  "))

doadores = {}

for i in range(qte_pessoas):
    nome_doador = input(f"Digite o nome do doador {i+1}:  ")
    valor_doacao = float(input(f"Digite o valor da doação de {nome_doador}: "))

    doadores[nome_doador] = valor_doacao

total_arrecadado = sum(doadores.values())

print("\n Dicionário de doações:")
for nome, valor in doadores.items():
    print(f" - {nome}: R${valor:.2f}")
print(f"\nTotal arrecadado: R${total_arrecadado:.2f}")
