#Questão 001-
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
    
    
