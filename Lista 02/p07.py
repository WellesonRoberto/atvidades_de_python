idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você nnão pode votar.")
elif idade >= 18 and idade <= 70:
    print("Voto obrigatório!")
else:
    print("Voto opcional.")
