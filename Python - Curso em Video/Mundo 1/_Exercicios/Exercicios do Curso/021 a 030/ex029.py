print('========== DESAFIO 029 ==========')
print('')

print('Escreva um programa que leia a velocidade de um carro. \nSe ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. \nA multa vai custar R$7,00 reais por cada km acima do limite.')
print('')

vel = int(input('\nPor favor digite a velocidade do carro: '))

if vel > 80:
    print('\nVocê foi multado!')
    vmulta = (vel - 80)*7
    print('\nO valor da multa é de R${}'.format(vmulta))
else:
    print('\nParabéns, você não foi multado!')