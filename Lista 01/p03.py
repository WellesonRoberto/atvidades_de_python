# 3) O CESAR deseja enviar uma mensagem aos seus funcionários
# informando sobre um bônus especial.
# Escreva um programa que receba o valor do salário mensal do
# funcionário e sobre esse salário, calcule um bônus de 10%.
# Ao final, imprima na tela o salário inicial, o salário final e
# quanto de acréscimo o funcionário recebeu em reais.

# Recebendo o valor do salário mensal do funcionário
salario_mensal = float(
    input("Digite o valor do salário mensal do funcionário: "))

# Calculando o bônus de 10%
bonus = salario_mensal * 0.1

# Calculando o salário final com o bônus
salario_final = salario_mensal + bonus

# Exibindo informações:
print("Salário inicial: R$:", salario_mensal)
print("Acréscimo recebido: R$", bonus)
print("Salário final com bônus: R$", salario_final)
