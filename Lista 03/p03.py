'''Faça um programa que receba notas de alunos, até -1 ser informado. Ao final,
o programa deve exibir quantas notas foram informadas e a média entre elas.'''

nota = 0.0
i = 0
soma_notas = 0.0

while nota != -1:
    nota = float(input("Digite uma nota ou -1 pra finalizar: "))

    if nota != -1:
        i = i + 1
        soma_notas = soma_notas + nota

media = soma_notas/i

print(f"Quantidade notas informadas: {i}")
print(f"Média do aluno: {media}")
