print('========== DESAFIO 034 ==========')
print('')

print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\npara salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais o aumento é de 15%.')
print('')

sal = float(input('\nDigite seu salário: '))

if sal > 1250:
    nsal = sal * 1.10
    print('\nParabéns, você recebeu um aumento de 10%\nSeu salário agora é de: R$ {:.2f}'.format(nsal))
else:
    nsal = sal * 1.15
    print('\nParabéns, você recebeu um aumento de 15%\nSeu salário agora é de: R$ {:.2f}'.format(nsal))
