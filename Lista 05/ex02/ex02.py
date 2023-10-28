'''Em um arquivo .txt existe uma quantidade de 10 valores que representam
medições de profundidade. Desenvolva um código que conte o número de vezes
que uma medição aumenta em relação à medição anterior. No exemplo abaixo, há
7 medições maiores que a anterior. 
O código deve permitir a escrita das medições no arquivo, e na sequência retornar
quantas são maiores que a anterior.'''

import os.path
import os
os.system("cls")


if os.path.exists("ex02/profundidades.txt") is False:
    print("Arquivo texte.txt não existe. Criando...")
    meuArquivo = open("ex02/profundidades.txt", "w")

meuArquivo = open("ex02/profundidades.txt", "r+")

valores = []

for i in range(10):
    profundidades = input("Digite a profundidade: ")

    meuArquivo.write(profundidades+"\n")

    aumentos = 0

    for i in range(i, len(profundidades)):
        if profundidades[i] > profundidades[i - 1]:
            aumentos += 1


print("\n Exibindo profundidades: ")
meuArquivo = open("ex02/profundidades.txt")
print(meuArquivo.read())
print(aumentos)
meuArquivo.close()
