'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
de números pares e a quantidade de números ímpares.'''

cont_par = 0
cont_impar = 0


for i in range(6):
    numero = int(input("Digite o número: "))
    if numero % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f"Números pares: {cont_par}")
print(f"Números ímpares: {cont_impar}")
