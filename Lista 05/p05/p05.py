arquivo = open("p05/arquivo.txt", "r")
soma = 0.0
quant = 0

for nota in arquivo:
  nota = float(nota)
  soma+=nota
  quant+=1

arquivo.close()

print(soma)
print(quant)

media = soma/quant
print(f"A média é {media}")