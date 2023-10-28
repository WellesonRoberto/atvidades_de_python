'''Uma empresa deseja reavaliar os salários dos seus funcionários.
Será reajustado o salário daqueles que estão há 2 anos ou mais
sem receber aumento.
O ajuste acontecerá da seguinte forma:
• Funcionário com mais de 10 anos de casa, 30%.
• Funcionário que tem entre 5 a 10 anos de casa, 20%.
• Funcionário com menos de 5 anos de casa, 10%.
Aqueles que receberam aumento salarial há menos de 2 anos não
estão aptos ao reajuste salarial coletivo.'''

from datetime import date
import os

os.system("cls")

ano_atual = date.today().year
ano_admissão = int(input("Digite o ano da admissão do funcionário: "))
salario_atual = float(input("Digite o salário atual: "))
ano_reajuste = int(input("Digite o último ano do reajuste salarial: "))

tempo_aumento = ano_atual - ano_reajuste
anos_trabalhados = ano_atual - ano_admissão

if tempo_aumento >= 2:
    if anos_trabalhados > 10:
        novo_salario = salario_atual*1.30
    elif anos_trabalhados >= 5 and anos_trabalhados <= 10:
        novo_salario = salario_atual*1.20
    else:
        novo_salario = salario_atual*1.10
    print("\nApto a receber reajuste salarial!")
    print(f"Novo salário: R${novo_salario:.2f}")
else:
    print("Não está apto para receber reajuse salarial.")
