'''Faça um programa que pergunte para um gerente de uma lanchonete se ele
deseja remover, adicionar ou modificar o valor de um produto do cardápio,
apenas encerrando o algoritmo quando o usuário decidir. No final, mostre o
cardápio com as modificações. Segue o cardápio original (já cria o
dicionário com esses valores):'''

produtos = {"coxinha": 5.00, "pastel": 4.00, "suco": 3.50, "bolo": 4.50}
print(produtos)

decisao = input("\nVocê deseja modificar o cardápio? [S] ou [N]: ")

while decisao == "S":
    pergunta = input(
        "\nVocê deseja Adicionar [A], Remover [R] ou Modificar [M] um produto?")

    if pergunta == "A":
        nome = input("Digite o nome do novo produto: ")
        valor = float(input("Digite o valor do novo produto: "))
        produtos[nome] = valor

    elif pergunta == "R":
        nome = input("Digite o nome do produto a ser removido: ")
        if produtos.get(nome):
            produtos.pop(nome)
        else:
            print("Produto não encontrado")

    elif pergunta == "M":
        nome = input("Digite o nome do produto que deseja alterar: ")
        valor = float(input("Digite o valor da alteração: "))
        if produtos.get(nome):
            produtos[nome] = valor
        else:
            print("Nome inválido.")

    else:
        print("Opção inválida.")

    decisao = input("Você deseja fazer mais alguma alteração? [S] ou N")

print()
print(produtos)
