# 6)Uma revendedora de carros usados paga a seus
# vendedores um salário fixo por mês, mais uma
# comissão também fixa para cada carro vendido e
# mais 5% do valor das vendas por ele efetuadas.

# Escreva um algoritmo que leia o número de
# carros vendidos por uma pessoa vendedora, o
# valor total de suas vendas, o salário fixo e a
# comissão que a pessoa receberá por carro
# vendido. Calcule e escreva o salário final.

carros_vendidos = int(input("Digite a quantidade de carros vendidos: "))
total_vendas = float(input("Digite o valor total em vendas: "))
salario_fixo = float(input("Digite seu salário fixo: "))
comissao = float(input("Digite o valor da comissão por carro vendido: "))

salario_final = salario_fixo + \
    (comissao * carros_vendidos) + (total_vendas * 0.05)

print(f"O salário final do vendedor foi: R${salario_final:.2f}")
