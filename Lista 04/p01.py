'''Desenvolva um programa que receba (o usuário insere)
cinco valores inteiros e guarde em um vetor (lista). Ao final,
mostre os valores na tela.'''

valores = []

for i in range(5):
    valores.append(int(input("Digite um valor: ")))
    # append = adiciona um valor novo

print(valores)
