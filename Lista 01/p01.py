# 1) Desenvolva um programa em que o professor possa inserir o
#    seu nome, o seu salário fixo e o total de aulas que ele
#    ministra por mês. Após isso, exiba na tela as informações.


nome = input("Digite o seu nome: ")
salario = float(input("Digite seu salário fixo: "))
aulas = int(input("Digite a quantidade de aulas: "))

print("O professor", nome, " recebe um salário de R$",
      salario, " e ministra", aulas, " por mês.")
