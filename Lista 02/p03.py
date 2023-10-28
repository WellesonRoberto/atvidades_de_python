'''3) Desenvolva um programa que pergunte a velocidade de um carro. Caso
a velocidade ultrapasse 80Km/h, exiba uma mensagem dizendo que o
usuário foi multado.
Nesse caso, exiba o valor da multa, cobrando R$ 5 por cada Km acima
da velocidade permitida.
2 ações possíveis:
1. Emitir a mensagem “Você foi multado e pagará R$ ….”
2. Encerrar o programa'''

velocidade = float(input("Digite a velocidade do veículo: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f"\nVocê foi multado! O valor da multa é de R${multa:.2f}")
