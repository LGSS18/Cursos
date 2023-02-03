print('========== DESAFIO 011 ==========')
print('')

print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².')
print('')

h = float(input('Digite a altura da parede: '))
b = float(input('Digite a largura da parede: '))
print('')

ap = h*b
lt = ap/2

print('uma parede de área {} precisará de {} litros de tinta'.format(ap, lt))
