arquivo = open("p07/arquivo.txt", "w")

disciplina = input("Qual disciplina você está cursando? ")
turma = input("Qual a sua turma? ")

arquivo.write(disciplina + "\n")
arquivo.write(turma)

arquivo.close()

arquivo = open("p07/arquivo.txt", "r")
print(arquivo.read())

arquivo.close()