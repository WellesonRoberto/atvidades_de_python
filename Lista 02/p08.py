'''8) Ao tentar colocar um Voltorb em uma piscina, Biu acabou levando
um choque do trovão. Curioso de saber qual foi a intensidade do
choque que levou, ele pesquisou e descobriu que existia uma
relação entre o level do voltorb e a potência de seu choque.
Escreva um programa que, dado o
level do voltorb, imprima de quanto
foi o choque em W segundo a tabela: (olhar no pdf)'''

level = int(input("Digite o level do voltorb: "))

if level >= 1 and level <= 20:
    potencia_choque = 20 + level**3

elif level >= 21 and level <= 40:
    potencia_choque = 8000 + (level - 10)**2

elif level >= 41 and level <= 60:
    potencia_choque = 9000 + 5*level

elif level >= 61 and level <= 80:
    potencia_choque = 9300 + 2*level

elif level >= 81 and level <= 100:
    potencia_choque = 9500 + level
else:
    print("Opção inválida!")

print(f"A potência do choque foi de {potencia_choque} W.")
