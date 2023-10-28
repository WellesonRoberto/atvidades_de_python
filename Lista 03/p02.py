'''Desenvolva um programa que permite ao usuário inserir os
valores dos produtos comprados por um cliente. O programa
deve terminar quando o usuário inserir o valor zero.
Se o usuário digitar um valor negativo, não deve ser
processado e um novo valor deve ser solicitado como
entrada.
ao final informe o valor total a pagar
Lembrando que, caso as vendas ultrapassem ao total de R$
1.000,00 deverá ser aplicado um desconto de 10%'''

total = 0

while True:  # enquanto for verdadeiro, irá executar o while
    valor = float(input("Digite o valor do produto (ou 0 pra encerrar): "))

    if valor < 0:
        print("Valor negativo não é permitido. Tente novamente.")
        continue
    elif valor == 0:
        break  # encerra o while quando digitar 0
    total += valor

if total > 1000:
    total *= 0.9

print(f"O valor total a pagar é: R${total:.2f}")
