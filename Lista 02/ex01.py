'''Faça um algoritmo que leia a primeira letra do estado civil de uma
pessoa e mostre uma mensagem com a sua descrição (Solteiro, Casado,
Viúvo, Divorciado). Mostre uma mensagem de erro, caso a opção seja
inválida.'''

estado_civil = input(
    "Digite a inicial do estado civil: [S]Solteiro, [C]Casado, [D]Divorciado e [V]Viúvo: ")

if estado_civil == "S":
    print("Esta pessoa é solteira.")
elif estado_civil == "C":
    print("Esta pessoa é casada.")
elif estado_civil == "V":
    print("Esta pessoa é viúva.")
elif estado_civil == "C":
    print("Esta pessoa é divorciada.")
else:
    print("Opção inválida.")
