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
    
    
