print('========== DESAFIO 015 ==========')
print('')

print('Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')
print('')

km1 = float(input('Favor informar a quantidade de km rodado: '))
dias1 = int(input('Informar quantos dias foi alugado: '))
print('')

kmt = km1 * 0.15
diast = dias1 * 60

print('O valor total desse aluguel é: R${:.2f}'.format(kmt+diast))
