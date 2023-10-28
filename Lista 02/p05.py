'''5) Desenvolva um programa que leia dois números e efetue a
adição. Caso o resultado seja maior que 10, este deverá
ser apresentado somando-se a ele mais 5; caso o
resultado seja menor ou igual a 10, este deverá ser
apresentado subtraindo-se 5.'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2

if soma > 10:
    print(f"Valor final:{soma+5}")
else:
    print(f"Valor final é: {soma-5}")
