# Escreva um programa para encontrar o fatorial de qualquer número.

print('-=' *25)
print('PROGRAMA PARA ENCONTRAR O FATORIAL DE UM NUMERO')
print('-=' *25)

number = int(input('Digite o numero: '))

fatorial = number

for f in range(1, number):
    fatorial = fatorial * f 
    
print(f'O fatorial desse numero é {fatorial}')