import os
os.system("cls") #limpa o terminal

arquivo = open("p06/arquivo.txt", "r", encoding="utf8")
dados = arquivo.read() # Transforma o conteúdo do arquivo em uma única string
palavras = dados.split() #Cria uma lista da string separando por um delimitador

arquivo.close()

print("Dados do arquivo:\n")
print(dados)
print()
print(palavras)
print(f"\nQuantidade de caracteres: {len(dados)}")
print(f"\nQuantidade de palavras: {len(palavras)}")
print()



