# Dicionário

'''
  o get(), no qual podemos passar como
parâmetros a chave que queremos e um valor padrão
para retornar caso essa chave não seja encontrada.
  pop(), além de remover o elemento com a chave
especificada do dicionário, nos retorna o valor desse
elemento. 
'''

agenda = {"Well": [999207356, 984948296], "Mom": [985950966]}

print(agenda["Well"])
print(agenda.get("Ana", "Não encontrado"))
print(agenda.pop("Mom", "Não encontrado"))
print(agenda)
