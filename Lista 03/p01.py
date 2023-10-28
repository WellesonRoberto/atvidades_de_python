'''Desenvolva um programa que some os números pares entre o
intervalo de dois números. O número inicial e o final do intervalo
são fornecidos pelo usuário. Caso esses valores sejam pares, eles
também entram na contagem.'''

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
soma = 0

while num1 <= num2:
    if num1 % 2 == 0:
        soma = soma + num1
    num1 += 1
print(f"A soma entre os números pares é: {soma}")
