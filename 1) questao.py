# Faça um programa que receba 10 números e conte quantos deles estão no intervalo [10,20] e quantos deles estão fora do intervalo, escrevendo estas informações.

print('-=' * 50)
print('PROGRAMA PARA ENCONTRAR A QUANTIDADE DE NUMEROS QUE ESTÃO ENTRE 10 E 20, E OS QUE ESTÃO FORA')
print('-=' * 50)
print('Digite 10 números, dentre eles irá aparecer os que estiverem entre 10 e 20 e os que estão fora \n')

dentro = []
fora = []

for n in range(10):
    num = int(input('Digite os números: '))

    if 10 <= num <= 20:
        dentro.append(num)
        count1 = len(dentro)

    else:
        fora.append(num)
        count2 = len(fora)
        
print('-=' * 45)
print(f'Existem {count1} números entre 10 e 20', f'e {count2} números fora.')