'''Desenvolva um programa utilizando o para que faça a tabuada de um número
inteiro que será digitado pelo usuário. Mas a tabuada não deve necessariamente
iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados pelo
usuário.
Segue um exemplo: Montar a tabuada do: 5
Começar por: 4
Terminar em: 7
Saída de dados:
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35'''

numero = int(input("Digite um número: "))
n_i = int(input("Digite o número que irá iniciar a tabuada: "))
n_f = int(input("Digite o número que irá finalizar a tabuada: "))

for resultado in range(n_i, n_f+1):
    print(f"{numero} x {resultado} = {resultado*numero}")
