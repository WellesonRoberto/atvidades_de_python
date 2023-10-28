notas = {"João": [9.0, 8.0], "Maria": [10.0, 2.0], "Pedro": [8.5, 5.0]}

for nome in notas:
    media = sum(notas[nome])/len(notas[nome])

    print(f"A média de {nome} é: {media}")
