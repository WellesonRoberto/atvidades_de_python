
import os

# Função para contar o número de vezes que uma medição é maior que a anterior


def contar_aumentos(profundidade):
    try:
        with open(profundidade, 'r') as file:
            lines = file.readlines()
            if len(lines) != 10:
                print("O arquivo deve conter exatamente 10 medições.")
                return 0

            medidas = [float(line.strip()) for line in lines]
            aumentos = 0

            for i in range(1, len(medidas)):
                if medidas[i] > medidas[i - 1]:
                    aumentos += 1

            return aumentos

    except FileNotFoundError:
        print(f"O arquivo '{profundidade}' não foi encontrado.")
        return 0
    except ValueError:
        print("O arquivo contém valores inválidos.")
        return 0

# Função para escrever medições em um arquivo


def escrever_medicoes(profundidade, medidas):
    with open(profundidade, 'w') as file:
        for medida in medidas:
            file.write(str(medida) + '\n')


# Exemplo de uso:
'''medicoes = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
escrever_medicoes('medicoes.txt', medicoes)
num_aumentos = contar_aumentos('medicoes.txt')
print(f"Número de medições maiores que a anterior: {num_aumentos}")'''
