'''Desenvolva um programa para calcular a redução do tempo de vida
de um fumante. Pergunte a quantidade média de cigarros fumados
por dia e por quantos anos ele já fumou. Considere que um fumante
perde 10 min de vida a cada cigarro. Calcule e exiba quantos dias de
vida o fumante perdeu até o momento.'''

cig_dia = int(input("Digite a média de cigarros fumados por dia: "))
anos_fumo = int(input("Anos fumando: "))

total_cig = cig_dia * (anos_fumo*365)
reducao_vida_dias = (total_cig*10)*6.94*10**-4


print(
    f"Total de cigarros fumados até agora: {total_cig}, durante {anos_fumo} ano(s).")
print(f"Vida perdida: {reducao_vida_dias} dias. ")
