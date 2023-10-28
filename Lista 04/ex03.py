'''Leia a idade de 4 pessoas e armazene-as em uma lista. Após esta entrada
de dados, exiba:
i) As idades armazenadas;
ii) Média das idades;
iii) Maior e menor idade (pode usar max e min);'''

import os
os.system("cls")

idades = []


for i in range(4):
    idades.append(int(input("Digite a idade da pessoa: ")))

print(idades)
print(f"A média das idades é {sum(idades)/len(idades)}")
print(f"A maior idade é {max(idades)} e a menor é {min(idades)}")
