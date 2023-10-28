'''Foi realizada uma pesquisa de algumas características físicas de 5 alunos de um
curso, a qual coletou os seguintes dados referentes a cada pessoa para serem
analisados:
sexo (masculino e feminino)
cor dos olhos (azuis, verdes ou castanhos)
cor dos cabelos ( louros, castanhos, pretos)
idade
Faça um algoritmo que determine e escreva:
a) a quantidade de pessoas do sexo feminino cuja idade está entre 18 e 35;
b) a quantidade de pessoas que têm olhos castanhos e cabelos pretos.'''

cont_feminino_idade = 0
cont_castanho_cabPreto = 0

for i in range(3):
    sexo = input("Digite o sexo do aluno [M] ou [F]: ")
    idade = int(input("Digite a idade do aluno: "))
    cor_olhos = input(
        "Digite a cor dos olhos do aluno: [A]Azuis, [V]Verdes ou [C]Castanhos. ")
    cor_cabelo = input(
        "Digite a cor do cabelo do aluno: [L]Louros, [C]Castanhos, [P]Pretos. ")
    print()

    if sexo == "F" and idade >= 18 and idade <= 35:
        cont_feminino_idade += 1

    if cor_olhos == "C" and cor_cabelo == "P":
        cont_castanho_cabPreto += 1


print(
    f"Existem {cont_feminino_idade} mulheres com idades entre 18 e 35 anos.")

print(
    f"Existem {cont_castanho_cabPreto} pessoas com olhos castanhos e cabelos pretos.")
