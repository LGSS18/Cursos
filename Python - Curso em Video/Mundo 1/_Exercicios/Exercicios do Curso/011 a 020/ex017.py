import math
print('========== DESAFIO 017 ==========')
print('')

print('Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.')
print('')

c1 = int(input('Informe a medida do cateto 1: '))
c2 = int(input('Informe a medida do cateto 2: '))
print('')

h = math.hypot(c1, c2)

print('A hipotenusa do triângulo de catetos {} e {} é igual a: {}'.format(c1, c2, h))
