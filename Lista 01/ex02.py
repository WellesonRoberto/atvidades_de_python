'''Escreva um programa que leia três valores com ponto flutuante: A, B e
C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem o valor de A como base e
o valor de C como altura.
b) a área do círculo que tem como raio o valor de C.
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem como lado o valor de B.
e) a área do retângulo que tem lados A e B.'''

valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
valorC = float(input("Digite o valor de C: "))
pi = 3.14

print(f"O valor da área de triângulo retângulo é: {(valorA *  valorC)/2}m2")
print(f"O valor da área do círculo é: {pi*(valorC)**2}m2")
print(f"O valor da área do trapézio é: {((valorA + valorB)*valorC)/2}m2")
print(f"O valor da área do quadrado é: {valorB*valorB}m2")
print(f"O valor da área de retângulo é: {valorA * valorC}m2")
