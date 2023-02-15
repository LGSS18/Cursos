print('========== DESAFIO 035 ==========')
print('')

print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo')
print('')

r1 = float(input('\nDigite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))


if r1 > (r2 - r3) and r1 < (r2 + r3):
    print('\nParabéns, as retas formam um triângulo')

if r1 > (r3 - r2) and r1 < (r2 + r3):
    print('\nParabéns, as retas formam um triângulo')

if r2 > (r1 - r3) and r2 < (r1 + r3):
    print('\nParabéns, as retas formam um triângulo')

if r2 > (r3 - r1) and r2 < (r1 + r3):
    print('\nParabéns, as retas formam um triângulo')

if r3 > (r2 - r1) and r3 < (r1 + r2):
    print('\nParabéns, as retas formam um triângulo')

if r3 > (r1 - r2) and r3 < (r1 + r2):
    print('\nParabéns, as retas formam um triângulo')