'''Sua organização acaba de contratar um estagiário para trabalhar no
Suporte de Informática, com a intenção de fazer um levantamento nas
sucatas encontradas nesta área. A primeira tarefa dele é testar todos os
mouses que se encontram lá, testando e anotando o estado de cada um
deles, para verificar o que se pode aproveitar.
Foi requisitado que você desenvolva um programa para registrar este
levantamento. O programa deverá receber a quantidade de mouses, o
número de identificação e o tipo de defeito de cada um, sendo eles:
● necessita da esfera;
● necessita de limpeza;
● necessita troca do cabo ou conector;
● quebrado ou inutilizado
Ao final o programa deverá emitir o seguinte relatório (exemplo):'''

import os
os.system("cls")

opcao1 = 0
opcao2 = 0
opcao3 = 0
opcao4 = 0
mouses = []

qte_mouses = int(input("Digite a quantidade de mouses: "))

for i in range(qte_mouses):
    id = int(input("Digite o número de idenficação do mouse: "))
    mouse = input(
        f"\n Qual a situação do mouse {i+1} ? \n1 - Necessita da esfera \n2 - Necessita de limpeza \n3 - Necessita de troca do cabo ou conector \n4 - Quebrado ou inutilizado \nResposta: ")

    if mouse == "1":
        opcao1 += 1
    elif mouse == "2":
        opcao2 += 1
    elif mouse == "3":
        opcao3 += 1
    elif mouse == "4":
        opcao4 += 1
    else:
        print("Opção inválida!")


mouses.append(opcao1)
mouses.append(opcao2)
mouses.append(opcao3)
mouses.append(opcao4)

total_mouses = opcao1 + opcao2 + opcao3 + opcao4
print()

print(
    f"Situação dos mouses: \n1 - Necessita de esfera: {opcao1} ({(opcao1*100)/total_mouses}%) \n2 - Necessita de limpeza: {opcao2} ({(opcao2*100)/total_mouses}%) \n3 - Necessita de troca do cabo ou conector: {opcao3} ({(opcao3*100)/total_mouses}%) \n4 - Quebrado ou inutilizado: {opcao4} ({(opcao4*100)/total_mouses}%)")
