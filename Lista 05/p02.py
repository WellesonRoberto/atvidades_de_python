'''Como citado anteriormente, utilizamos o join()
quando a string está em uma lista. Dessa forma,
pode-se utilizar o comando split() previamente'''

nome = input("Digite seu nome completo: ")

novo_nome = nome.split()
print(novo_nome)
print(", ".join(novo_nome))