'''Crie um programa que escreva na tela a seguinte String:
'Python rainha, portugol nadinha'
a) Com todas as letras maiúsculas;
b) Com todas as letras minúsculas;
c) Apenas com a primeira letra maiúscula;
d) A primeira letra de cada palavra maiúscula;
e) Quantas vezes a letra “a" se repete na string;
f) Uma nova string na qual a palavra “nadinha” seja trocada por “ ”.'''

frase = "Python rainha, portugol nadinha"

print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.count("a"))
nova_frase = frase.replace("nadinha", "princesinha")
print(nova_frase)