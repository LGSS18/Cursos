import math
print('========== DESAFIO 016 ==========')
print('')

print('Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.')
print('')

num = float(input('Digite um número real: '))
print('')

x = math.trunc(num)

print('A porção inteira de {} é igual a {}'.format(num, x))
