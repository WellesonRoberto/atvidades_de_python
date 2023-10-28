'''Desenvolva um programa que seja capaz de calcular a média
ponderada de um aluno. Inicialmente solicite o nome e as três notas
do aluno, logo após, calcule e exiba na tela a média. Na média
ponderada considere os seguintes pesos nas notas: 2, 3 e 5. Essa é a
fórmula para calcular a média.

Logo após verifique e informe o status do aluno na disciplina
baseando nas seguintes informações:
Média até 4.9: reprovado
Média entre 5.0 e 6.9: recuperação
Média 7.0 ou superior: aprovado'''


nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

mediafinal = (nota1*2 + nota2*3 + nota3*5)/10

print(f"A média final do aluno é {mediafinal:.2f}")

if mediafinal <= 4.9:
    print("Aluno(a) reprovado(a).")
elif mediafinal >= 5.0 and mediafinal <= 6.9:
    print("Alun(a) em recuperação.")
else:
    print("Aluno(a) aprovado(a).")
