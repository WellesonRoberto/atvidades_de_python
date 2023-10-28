'''A conta de energia elétrica de consumidores residenciais de uma cidade é
calculada do seguinte modo:
• se o consumo é de até 500 kw, a tarifa é de R$ 0,02 por unidade de kw;
• se o consumo é maior que 500 kw, mas não excede 1000 kw, a tarifa é
de R$10,00 por unidade de kw;
• se o consumo é maior que 1000kw, a tarifa é de R$35,00 por unidade
de kw;
• em toda conta, é cobrada uma taxa básica de serviço de R$5,00,
independentemente da quantidade de energia consumida.
Escreva um programa que leia o consumo de energia de uma residência e
imprima o valor da sua conta de energia.'''

consumo_energia = int(input("Digite o valor do consumo de energia: "))

if consumo_energia < 500:
    print(
        f"A conta de energia dessa residência é de :R${consumo_energia * 0.02 + 5:.2f}")
elif consumo_energia > 500 and consumo_energia < 1000:
    print(
        f"A conta de energia dessa residência é de :R${consumo_energia * 10 + 5:.2f}")
else:
    print(
        f"A conta de energia dessa residência é de :R${consumo_energia * 35 + 5:.2f}")
