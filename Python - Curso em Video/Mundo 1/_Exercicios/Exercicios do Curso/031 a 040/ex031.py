print('========== DESAFIO 031 ==========')
print('')

print('Desenvolva um programa que pergunte a distância de uma viagem em km.\nCalcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km\n e R$0,45 para viagens mais longas.')
print('')

km = int(input('\nPor favor informe quantos km tem a viagem: '))

if km <= 200:
    vp1 = km * 0.5
    print('\nO valor da passagem é de R$ {}.'.format(vp1))
else:
    vp2 = km * 0.45
    print('\nO valor da passagem é de R$ {}.'.format(vp2))
