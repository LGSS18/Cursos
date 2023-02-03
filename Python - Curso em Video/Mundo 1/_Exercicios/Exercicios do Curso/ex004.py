print('========== DESAFIO 004 ==========')
print('')

print('Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.')
print('')

algo = input('Digite algo por favor: ')
print('')

#O que eu pensei por mim:
print('{} é uma letra: {}'.format(algo, algo.isalpha()))
print('{} é um alfanumérico: {}'.format(algo, algo.isalnum()))
print('{} é um número: {}'.format(algo, algo.isnumeric()))
print('{} está em maúiscula: {}'.format(algo, algo.isupper()))
print('')

#O que eu tentei com o video
print('{} esta vazia: {}'.format(algo, algo.isspace()))
print('{} está em minúscula: {}'.format(algo, algo.islower()))
print('{} está capitalizada: {}'.format(algo, algo.istitle()))
print('O tipo primitivo de {} é: {}'.format(algo, type(algo)))
