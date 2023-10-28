#Formatação de Strings - Tipo Inteiro

valor = int(input("Digite um valor: "))

print("Valor em binário: {0:b}".format(valor))
print("Valor na tabela ASCII: {0:c}".format(valor))
print("Valor na casa decimal: {0:d}".format(valor))
print("Valor na casa octal: {0:o}".format(valor))
print("Valor na casa hexadecimal: {0:X}".format(valor))
print()

#Formatação de Strings - Tipo float

print("Valor em notação científica: {0:e}".format(12.867))
print("Valor em notação científica: {0:E}".format(12.867))
print("Valor com 6 casas decimais por padrão: {0:f}".format(12.8677890123456))
print("Valor arrendodando as casas decimais: {0:g}".format(12.86789076543))
print("Valor multiplicadp por 100: {0:f}".format(12.867))