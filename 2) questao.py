#Crie um programa para contar a quantidade de números pares e ímpares de uma série de números.

print('-=' *40)
print('PROGRAMA PARA ENCONTRAR A QUANTIDADE DE NUMEROS PAR E ÍMPAR DE UMA SEQUENCIA')
print('-=' *40)
print('\nDigite uma serie de 8 numeros, no final irá ver quantos pares e impares tem nessa serie\n')

num = []
par = []
impar = []

for m in range(8):
    number = int(input('Digite um numero: '))
    num.append(number)

    if number % 2 == 0:
        par.append(number)
        count1 = len(par)

    else:
        impar.append(number)
        count2 = len(impar)
        
print(' ')
print(f'Os numeros digitados foram {num}\n'
f'Entre eles tem {count1} numeros pares, sendo {par}\n'
f'Entre eles tem {count2} numeros ímpares, sendo {impar}')