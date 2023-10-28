'''Faça um programa que calcule as raízes de uma equação do
segundo grau, na forma ax² + bx + c. O programa deverá perguntar
ao usuário de quantas equações ele deseja calcular as raízes, e na
sequência solicitar os valores de a, b e c.
Considere as seguintes situações:

1. Se o usuário informar o valor de A igual a zero, a equação não é do
segundo grau e o programa não deve pedir os demais valores (b e c)
ao usuário;
2. Se o delta calculado for negativo, a equação não possui raízes
reais. Informe ao usuário;
3. Se o delta calculado for igual a zero a equação possui apenas
uma raiz real; informe ao usuário o valor da raiz;
4. Se o delta for positivo, a equação possui duas raiz reais;
informe-as ao usuário;
PS: digite 'import math' no início do seu código. Para achar a raiz
quadrada da variável x, faça: math.sqrt(x)'''


import math

print("Calcule a equação do 2º grau ax² + bx + c")

quant = int(input("De quantas equações você gostaria de calcular as raízes? "))

for i in range(quant):
    a = int(input("Digite o valor de a: "))
    if a == 0:
        print("Se a=0, não é uma equação do 2º grau")
    else:
        b = int(input("Digite o valor de b: "))
        c = int(input("Digite o valor de c: "))
        delta = b**2 - 4*a*c

    if delta < 0:
        print("Delta menor que zero não possui raízes")
    elif delta == 0:
        raiz = -b/(2*a)
        print(f"Delta igual a zero possui uma única raiz, sendo ela: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta))/(2*a)
        raiz2 = (-b - math.sqrt(delta))/(2*a)
        print(f"Raízes: {raiz1} e {raiz2}")
