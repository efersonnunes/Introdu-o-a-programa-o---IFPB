##QUESTÃO 001##

for i in range (5,51):      # Primeiro Múltiplo é 5
    if i % 5 == 0:          # Formula 
        print(i)

##QUESTÃO 002##

for i in range (100, -10, -10):
    print(i)
    
#QUESTÃO 003##

n = int(input('N: '))
n = n + 1
soma = 0
cont = 0
while n > 1:
    n = n - 1
    soma = soma + n
    cont = cont + 1
print(f'Soma dos {cont} números é : {soma}')
    
##QUESTÃO 005##

numero = int(input('N°'))
maior = numero
menor = numero
for i in range (99):
    numero = int(input('N°'))
    if numero > maior :
        maior = numero
    if numero < menor :
        menor = numero
print('Maior Número: ',maior,'\nMenor Número :',menor)
    
## Questão 006 ##
while True:
    senha = 12345678
    entrada = int(input('Senha:'))
    if senha == entrada:
        print('Correto')
        break
    else:
        print('Incorreta')
## Questão 007 ## 
n = int(input('N° :'))
n = n + 1
fat = 1
while n > 1:
    n = n - 1
    fat = fat * n
print(f'Fatorial  é {fat}')

## Questão 008

while True:
    mat = int(input('Matricula :'))
    if mat == 0:
        break
    nome = input('Nome:')
    soma = 0
    for i in range (2):
        nota = int(input('Nota :'))
        soma = soma + nota
        media = soma / 2
        if media > 7:
            resultado = 'Aprovado'
        else:
            resultado = 'Reprovado'
    print('==' * 20)
    print(f'Matricula {mat}\nNome: {nome}\nNotas: {nota}\nResultado : {resultado} ')
    print('==' * 20)

    
    
