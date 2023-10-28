'''Crie um programa que leia vários números digitados pelo usuário e mostre nofinal o somatório entre eles. Obs: O programa será interrompido quando o
número 1111 for digitado.'''

soma = 0


while True:
    numero = int(input("Digite um número: "))
    if numero == 1111:
        break

    soma += numero


print(soma)
