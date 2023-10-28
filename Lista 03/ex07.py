'''Peça ao usuario que informe um número, logo após, calcula e exibe o fatorial do
número digitado. O fatorial de um número é calculado multiplicando todos os
valores inteiros entre o próprio número e 1.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

n = int(input("Digite um número: "))


fatorial = 1
i = 2

while i <= n:
    fatorial = fatorial * i
    i = i + 1

print(fatorial)
