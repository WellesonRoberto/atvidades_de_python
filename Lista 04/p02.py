'''As funções min(), max() e sum() encontram o menor valor da
lista, maior valor da lista e realiza a soma de todos os
elementos da lista, respectivamente. len() é o tamanho da lista.'''

notas = [6.0, 8.5, 4.5, 10.0, 9.5]

print(f"A menor nota foi: {min(notas)}")
print(f"A maior nota foi: {max(notas)}")
print(f"A soma das notas foi: {sum(notas)}")
print(f"A média da turma foi: {sum(notas)/len(notas)}")
