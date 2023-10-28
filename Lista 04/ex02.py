'''Sua missão é auxiliar os atletas da School, escreva um programa que
receba o nome e o tempo (em minutos) de três voltas de 5 corredores e
armazene tais tempos em um dicionário, onde a chave é o nome do
corredor, e os valores são os minutos de cada volta. Por fim, deverá ser
mostrado a média (com três casas decimais) de tempo de cada corredor e
o nome (todo em maiúsculo) do corredor que obteve a menor média.'''

# Criando um dicionário para armazenar os tempos dos corredores
tempos_corredores = {}

# Pedindo os dados dos corredores e armazenando no dicionário
for i in range(2):
    nome_corredor = input(
        f"Digite o nome do corredor {i + 1}: ").strip().upper()
    tempos = []
    for j in range(3):
        tempo = float(
            input(f"Digite o tempo da volta {j + 1} em minutos para {nome_corredor}: "))
        tempos.append(tempo)
    tempos_corredores[nome_corredor] = tempos

# Calculando a média de tempo de cada corredor
medias_corredores = {}
for corredor, tempos in tempos_corredores.items():
    media = sum(tempos) / len(tempos)
    medias_corredores[corredor] = round(media, 3)

# Encontrando o corredor com a menor média
corredor_menor_media = min(medias_corredores, key=medias_corredores.get)

# Mostrando as médias e o corredor com a menor média
print("\nMédias de tempo dos corredores:")
for corredor, media in medias_corredores.items():
    print(f"{corredor}: {media} minutos")

print(
    f"\nO corredor com a menor média de tempo é {corredor_menor_media} com uma média de {medias_corredores[corredor_menor_media]} minutos.")
