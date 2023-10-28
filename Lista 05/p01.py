'''Existem várias formas de concatenar Strings para
saída de dados, sendo elas:'''

nome = "Irineu"
sobrenome = "Você não sabe nem eu"

print(f"{nome}, {sobrenome}")
print(nome, sobrenome)
print(nome + ", " + sobrenome)
print("{}, {}".format(nome, sobrenome))
print()
'''O método replace() é utilizado para substituir um ou mais trechos
em uma string. Ele contém parâmetros para auxiliar a forma de
substituição desse conteúdo'''
print()
teste = "Sorria! Hoje é segunda!"
novo_teste = teste.replace("Sorria", "Força")
print(novo_teste)
print(novo_teste.upper()) #Coloca todas as letras maísculas
print(novo_teste.lower()) #Coloca todas as letras minúsculas
print(novo_teste.capitalize()) #Converte apenas a primeira letra da string em maiúsculo
print(novo_teste.title()) #converte a primeira letra de todas as palavras em maísculos
print(novo_teste.count("a"))# Retorna quantas vezes um caractere ou palavra aparece na string

print(novo_teste.split(), "\n") #Criar uma lista da string separando por um delimitador
print(novo_teste.lstrip()) ##Remove espaços em branco na esquerda
print(novo_teste.rstrip()) #Remove espaços em branco na direita de uma string
print(novo_teste.strip()) #Remover espaços em branco em ambos os lados de uma string respectivamente
print()
#União de strings

colaboradores = ["Mike", "Sofia", "Helen"]

print(colaboradores)
print(", ".join(colaboradores))
print(" - ".join(colaboradores))
print("".join(colaboradores))