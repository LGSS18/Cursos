print('========== DESAFIO 030 ==========')
print('')

print('Crie um programa que leia um número e mostre na tela se ele é par ou ímpar.')
print('')

num = int(input('\nPor favor digite um número: '))

if num == 0:
    print('\nNão tem como dividir 0.')
else:
    resto = num % 2
    if resto == 0:
        print('\nO número {} é par'.format(num))
    else:
        print('\nO número {} é ímpar'.format(num))
