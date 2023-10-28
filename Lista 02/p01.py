valor_compra = float(input("Digite o valor da compra: "))
cupom = input("Digite o cupom de desconto: ")

if cupom == "CESAR" or cupom == "CESARSCH":
    valor_final = valor_compra - (valor_compra*0.15)
    print("\n O valor da sua compra após o desconto é de: R$", valor_final)
