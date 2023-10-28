# 2) Desenvolva um programa que declare duas variáveis
#  chamadas altura e peso. A essas variáveis, atribua os valores
#  1.65 e 56Kg. Na sequência, peça ao usuário para inserir a
#  informação se ele pratica atividades físicas e quantos litros
#  de água ele bebe por dia. Exiba todas as informações na tela.

altura = 1.65
peso = 56.0

atividade = input("Você pratica atividade física?")
litros = float(input("Quantos litros de água você bebe por dia?"))

print("O jovem de ", altura, " de altura e ", peso, "KG, ele pratica atividade física?",
      atividade, ". E bebe ", litros, " litros de água por dia!\n")
