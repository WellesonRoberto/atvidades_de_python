'''Faça um programa que ao usuário informar a idade do atleta ele exiba
na tela qual a sua categoria, conforme a lista a seguir:
Juvenil – idade entre 16 e 18 anos;
Infantil – idade entre 14 e 15 anos;
Mirim – idade entre 12 e 13 anos;
Pré-Mirim – idade entre 10 e 11 anos.
Caso a idade não se enquadre em nenhuma categoria, exiba a
mensagem: “Categoria não registrada”.'''

idade = int(input("Digite a idade do atleta: "))

if idade >= 16 and idade <= 18:
    print("Categoria juvenil.")
elif idade == 14 or idade == 15:
    print("Categoria infatil.")
elif idade == 12 or idade == 13:
    print("Categoria mirim.")
elif idade == 10 or idade == 11:
    print("Categoria pré-mirim.")
else:
    print("Categoria não registrada.")
