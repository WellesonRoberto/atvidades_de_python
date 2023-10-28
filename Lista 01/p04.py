# 4) Desenvolva um programa que solicite que o aluno insira a
# sua idade e que a professora insira o seu salário. Na
# sequência, mostre na tela se é Verdadeiro ou Falso que:

# ● O aluno é maior de idade;
# ● O professor recebe mais que um salário mínimo.

# Obs: sem utilizar condicionais, apenas o comando print

# Solicita a idade do aluno e o salário do professor

idade_aluno = int(input("Digite a idade do aluno: "))
salario_professor = float(input("Digite o salário do professor: "))

# Imprime os resultados
print("É verdadeiro que o aluno é maior de idade?", idade_aluno >= 18)
print("É verdadeiro que o professor recebe mais que um salário mínimo?",
      salario_professor > 1320.00)
