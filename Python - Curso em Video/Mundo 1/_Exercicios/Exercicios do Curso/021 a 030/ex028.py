import random
from time import sleep
print('========== DESAFIO 028 ==========')
print('')

print('Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e\n5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.\n O programa deverá escrever na tela se o usuário venceu ou perdeu.')
print('')

num = random.randint(0, 5)

num2 = int(input('Por favor digite um número de 1 a 5: '))
sleep(3)

if num2 > 5:
    print('\nO número digitado foi maior que 5, favor tente novamente.')
else:
    if num2 == num:
        print('\nParabéns você acertou o número!')
    else:
        print('\nPuxa que pena, você errou!')
