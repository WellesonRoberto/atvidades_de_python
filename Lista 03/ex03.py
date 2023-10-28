'''Um petshop atende 5 cachorros por tarde. Faça um programa que solicite ao
usuário o código do serviço efetuado: (1 - banho; 2 - tosa; 3 - banho e tosa; 4-
outros). Por fim, exiba a quantidade de solicitações para cada um deles.'''

cont_banho = 0
cont_tosa = 0
cont_banho_tosa = 0
cont_outros = 0

for i in range(5):
    servico = input(
        "Digite o serviço que deseja: (1 - banho; 2 - tosa; 3 - banho e tosa; 4-outros: ")

    if servico == "1":
        cont_banho += 1
    elif servico == "2":
        cont_tosa += 1
    elif servico == "3":
        cont_banho_tosa += 1
    elif servico == "4":
        cont_outros += 1
    else:
        print("Opção inválida.")

print(
    f"Serviços pra esta tarde:\nBanho: {cont_banho} \nTosa: {cont_tosa}\nBanho e tosa: {cont_banho_tosa}\nOutros: {cont_outros}")
