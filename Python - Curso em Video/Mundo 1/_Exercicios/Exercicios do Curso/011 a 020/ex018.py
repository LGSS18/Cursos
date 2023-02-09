import math
print('========== DESAFIO 018 ==========')
print('')

print('Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
print('')

ang = float(input('Informe o ângulo escolhido: '))
print('')

cos = math.cos(math.radians(ang))
sen = math.sin(math.radians(ang))
tan = math.tan(math.radians(ang))

print('Com um ângulo de {}º temos um cosseno de {:.2f}, um seno de {:.2f} e uma tangente de {:.2f}'. format(ang, cos, sen, tan))
