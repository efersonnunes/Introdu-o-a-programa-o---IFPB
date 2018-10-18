#Questão 001->
print('''    1 - SAUDAÇÃO
    2 - BRONCA
    3- FELICITAÇÃO
    0 - FIM
''')
opcao = int(input('Opcão :'))
while opcao != 0: 
    if opcao == 1:
        print('Olá como Vai')
    elif opcao == 2:
        print('Vamos Estudar mais')
    elif opcao == 3:
        print('Meus Parabéns')
    opcao = int(input('Opcão :'))
    
    
#Questão 002 ->
while True:
    num = int(input('Número :'))
    if num % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
    opcao = input('Continuar: S/N').upper()
    if opcao == 'N':
        break
        
     # Questão 003 - 
    temperatura = int(input('Temperatura :'))
data = (input('Dia: '))
diaFrio = data
diaQuente = data
tempMaior = temperatura
tempMenor = temperatura
for i in range(29):
    temperatura = int(input('Temperatura'))
    data = (input('Dia: '))
    if temperatura > tempMaior:
        tempMaior = temperatura
        diaQuente = data
    if temperatura < tempMenor:
        tempMenor = temperatura
        diaFrio = data
print('== * 20')
print(f'Tem Mais Quente : {tempMaior} -> Dia  - {diaQuente} de Abril  \nTemp Mais Fria : {tempMenor} ->  Dia - {diaFrio} de Abril')
    
    
  
