'''Após o usuário digitar um número
inteiro, informe se ele é um número
perfeito.
Um número é perfeito se a soma dos
seus divisores (exceto ele) for igual ao
próprio número. Ex: : 6 é perfeito, pois
1+2+3 = 6.'''

n = int(input("Digite o valor de n: "))

soma = 0

# i representa os divisores do número
for i in range(1, n):
    if n % i == 0:
        soma+1

if n == soma:
    print(f"O número {n} é perfeito")
else:
    print(f"O número {n} não é perfeito.")
