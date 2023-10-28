import os
os.system("cls")

dados = []

arquivo = open("p08/arquivo.txt", "w", encoding="utf8")

for i in range(5):
  dados.append(input("Digite o nome do voluntário: "))

arquivo.writelines("\n".join(dados)) #Converte uma lista em string

arquivo.close()
print(dados)