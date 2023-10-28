'''6) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar
descontos para todos, mas especialmente para as mulheres. Faça um
programa que leia nome, sexo (F ou M) e o valor das compras do cliente e
calcule o desconto. Sabendo que:

● Se for mulher, ganha 13% de desconto
● Senão, ganha 5% de desconto

2 ações possíveis:
1. Aplicar 13% de desconto
2. Aplicar 5% de desconto

Obs: Considere que poderá ser digitado o sexo em maiúsculo
ou minúsculo'''

nome = input("Digite o nome do cliente: ")
sexo = input("Digite o sexo do cliente(F ou M): ")
valor_compras = float(input("Digite o valor das compras do cliente: "))


if sexo == 'F':
    valor_final = valor_compras - valor_compras * 0.13
    print(f"O valor da compra foi de R${valor_final:.2f}")
else:
    valor_final = valor_compras - valor_compras * 0.05
    print(f"O valor da compra foi de R${valor_final:.2f}")
