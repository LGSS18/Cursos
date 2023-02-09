print('========== DESAFIO 023 ==========')
print('')

print('Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos seus digitos separados.')
print('')

num = int(input('Digite o número: '))
print('')

milhar = num // 1000 % 10
centena = num // 100 % 10
dezena = num // 10 % 10
unidade = num // 1 % 10

print(milhar)
print(centena)
print(dezena)
print(unidade)
