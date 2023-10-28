'''Desenvolva um programa que receba o nome de um ciclista, a
distância que ele percorreu em Km e o tempo que ele gastou nesse
percurso, em horas. O programa deverá calcular a velocidade média
do ciclista e, exibi-la na tela duas vezes, uma em Km/h e a outra em
m/s. Dividimos por 3,6 quando queremos converter Km/h para m/s.'''

nome = str(input("Digite seu nome: "))
distancia = float(input("Digite a distância percorrida em km: "))
tempo = float(input("Digite o tempo gasto em horas: "))

vel_mediaKMH = distancia/tempo
vel_mediaMS = vel_mediaKMH/3.6

print(f"A velocidade média do ciclista em Km/h foi de {vel_mediaKMH:.2f}.")
print(f"A velocidade média do ciclista em m/s foi de {vel_mediaMS:.2f}.")
