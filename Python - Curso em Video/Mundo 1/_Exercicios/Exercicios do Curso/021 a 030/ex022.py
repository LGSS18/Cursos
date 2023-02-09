print('========== DESAFIO 022 ==========')
print('')

print('Crie um programa que leia o nome completo de uma pessoa e mostre:')
print('1 - O nome dela com todas as letras em maiúscula.')
print('2 - O nome dela com todas as letras em minúscula.')
print('3 - Quantas letras ao todo (sem considerar espaços).')
print('4 - Quantas letras tem o primeiro nome.')
print('')

nome = input('Digite seu nome: ')
nse = nome.replace(' ', '')
pnome = nome.split()
print('')

print('1 - {}'.format(nome.upper()))
print('2 - {}'.format(nome.lower()))
print('3 - {}'.format(len(nse)))
print('4 - {}'.format(len(pnome[0])))
