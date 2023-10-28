'''Desenvolva um programa que receba as notas de 5 alunos e, na sequência
calcule e informe a média;
Além disso, mostre na tela as notas que são superiores à média da turma'''

notas = []

for i in range(5):
    notas.append(float(input("Digite a nota do aluno: ")))

media = sum(notas)/5
print(f"A média da turma é: {media}")

for nota in notas:
    if nota > media:
        print(f"A nota {nota} foi maior que a média.")
