'''A fabricação dos presentes para o Natal é um processo muito
complicado. Diversas vezes os duendes ficam até tarde trabalhando
para que tudo possa ser terminado a tempo e com perfeição. Para
melhor gerenciar seus cronogramas, os duendes estipularam quantos
minutos são necessários para fabricar cada presente.
Já está quase no final do expediente, e um dos duendes pediu suaajuda. Faltam N minutos para a hora de ir embora, e restam dois
presentes para o duende Ed fabricar. Solicite quantos minutos faltam, e
quanto tempo é necessário para fabricar cada um dos presentes.
Ajude-o a descobrir se conseguirá fabricar os dois ainda hoje, ou se
deve deixar para amanhã.'''

mnts_faltando = int(
    input("Quantos minutos faltam para encerrar o expediente?"))
fab_presente = int(input("Quantos minutos é feito cada presente? "))

if mnts_faltando > (fab_presente)*2:
    print("Os presentes conseguem ser finalizados ainda hoje!")
else:
    print("Os presentes não conseguem ser finalizados hoje.")
