# 7) Peça ao usuário para inserir a temperatura em Fahrenheit.
# Na sequência, calcule e exiba na tela a temperatura em Celsius.

temperatura_F = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (temperatura_F - 32)/1.8

print(f"A tempera em celsius é: {celsius:.2f}")
