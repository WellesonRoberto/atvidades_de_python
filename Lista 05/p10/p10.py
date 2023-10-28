'''Crie um programa simples que pergunta se a pessoa deseja ler um
arquivo ou escrever algo nele. Nosso script vai funcionar assim:
Aparece um menu de opções (sair, ler ou escrever).
Se digitar ler, lê o conteúdo do arquivo e exibe na tela.
Se optar por escrever, escreve algo no arquivo.'''

import os.path

op = 1
while op:
    if os.path.isfile("p10/teste.txt") is False:
        print("Arquivo texte.txt não existe. Criando...")
        meuArquivo = open("p10/teste.txt", "w")

    meuArquivo = open("p10/teste.txt", "r+")

    print("\nMenu de opções:\n")
    op = int(input("0. Sair\n"
                   "1. Ler\n"
                   "2. Escrever\n"
                   "\nEscolha sua opção: "))

    if op == 1:
        print("\n", meuArquivo.read())
        meuArquivo.close()
    elif op == 2:
        meuArquivo = open("p10/teste.txt", "a")
        num = input("Digite um número: ")
        meuArquivo.write(num + "\n")
        meuArquivo.close()

meuArquivo.close()
