# Crie um programa que receba uma string como entrada e mostre a quantidade de números e letras. Caso não seja letra ou número, ignore.

print('-=' *40)
print('PROGRAMA PARA ENCONTRAR A QUANTIDADE DE NUMEROS E LETRAS DE UMA STRING')
print('-=' *40)

word = []
number = []

frase = str(input('Digite uma frase com numeros e letras: '))

for f in frase:
    if f.isdigit():
        number.append(f)
        count1 = len(number)

    elif f.isalpha():
        word.append(f)
        count2 = len(word)
        
print(f'\nTem {count1} numeros nesta frase\n'f'Tem {count2} letras nessa frase')