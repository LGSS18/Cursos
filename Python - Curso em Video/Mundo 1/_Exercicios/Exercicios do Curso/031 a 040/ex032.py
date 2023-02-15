print('========== DESAFIO 032 ==========')
print('')

print('Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')
print('')

ano = int(input('\nPor favor digite um ano: '))

if ano % 400 == 0:
    print('\nÉ um ano bissexto!')
else:
    if ano % 4 == 0:
        if ano % 100 == 0:
            print('\nNão é um ano bissexto!')
        else:
            print('\nÉ um ano bissexto!')
    else:
        print('\nNão é um ano bissexto!')
