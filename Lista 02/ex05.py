'''Índice de Massa Corpórea (IMC) é um valor calculado baseado na
altura e no peso de uma pessoa. De acordo com o valor do IMC,
podemos classificar o indivíduo dentro de certas faixas:
Menor que 18.5: Abaixo do peso
Entre 18.5 e 24.9: Peso ideal
Entre 25 e 29.9: Sobrepeso
Entre 30 e 39.9: Obesidade
40 ou mais: Obesidade mórbida
Solicite a altura e o peso do usuário, calcule o seu IMC e mostre a
classificação. O IMC é calculado pela expressão peso/altura² (peso
dividido pelo quadrado da altura).'''

peso = float(input("Digite o peso do paciente: "))
altura = float(input("Digite a altura do paciente: "))

imc = peso / (altura)**2

if imc < 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso ideal.")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso.")
elif imc >= 30 and imc <= 39.9:
    print("Obesidade.")
else:
    print("Obesidade mórbida.")
