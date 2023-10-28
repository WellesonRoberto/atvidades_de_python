'''Desenvolva um programa que leia a largura e altura de uma parede,
calcule e mostre a área a ser pintada e a quantidade de tinta
necessária para o serviço, sabendo que cada litro de tinta pinta uma
área de 2 metros quadrados (m²).'''

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura

qte_tinta = area/2

print(
    f"A parede possui {area}m2 e serão necessários {qte_tinta}L de tinta para pintar toda parede!")
