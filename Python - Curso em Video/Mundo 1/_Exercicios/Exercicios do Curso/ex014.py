print('========== DESAFIO 014 ==========')
print('')

print('Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.')
print('')

celsius = float(input('Digite a temperatura em graus celsius: '))
print('')

fahre = (celsius * 1.8)+32

print('{:.1f}º celsius é igual a {:.1f}º fahrenheit'.format(celsius, fahre))
