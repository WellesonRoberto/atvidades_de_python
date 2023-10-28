'''Faça um programa que peça ao usuário para inserir:
○ uma frase
○ uma palavra que está contida na frase
○ outra palavra que ele deseja substituir no lugar da primeira palavra inserida.
Por fim, o programa exibe a frase modificada, toda em letra maiúscula.'''

frase = input("Digite uma frase: ")

palavra = input("Digite uma palavra para substiuir: ")
nova_frase = frase.replace("vida", palavra)
print(nova_frase.upper())
