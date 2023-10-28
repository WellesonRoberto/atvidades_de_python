import os

# Função para verificar se um endereço IP é válido


def ip_valido(ip_string):  # função que vai receber uma string
    partes = ip_string.split('.')
    if len(partes) != 4:  # se o tamanho for diferente de 4
        return False  # irá retornar falso
    for parte in partes:  # pra cada parte do ip
        if not parte.isdigit():  # irá ser conferido se o ip é feito só de dígitos numéricos
            return False  # retorna falso
        parte_integer = int(parte)  # interpretar a parte como um inteiro
        if parte_integer < 0 or parte_integer > 255:  # se aparecer nessa condição
            return False  # retorna falso
    return True

# Função para ler e verificar os IPs de um arquivo


if os.path.exists("ex04/ips.txt"):
    ips = open("ex04/ips.txt", "r")
    lista_ips = ips.read().split("\n")

    validos = []
    invalidos = []

    for ip in lista_ips:
        if ip_valido(ip) == True:
            validos.append(ip)
        else:
            invalidos.append(ip)

    if len(validos) > 0 or len(invalidos) > 0:
        arquivo_relatorio = open("ex04/resposta.txt", "wt")

        if len(validos) > 0:
            arquivo_relatorio.write("[Endereços válidos:]\n")
            for valido in validos:
                arquivo_relatorio.write(valido+"\n")
        if len(invalidos) > 0:
            arquivo_relatorio.write("\n[Endereços inválidos:]\n")
            for invalido in invalidos:
                arquivo_relatorio.write(invalido+"\n")

        arquivo_relatorio.close()
