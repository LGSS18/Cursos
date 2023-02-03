print('========== DESAFIO 010 ==========')
print('')

print('Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.')
print('')

money = float(input('Valor na carteira: '))
print('')

c327 = money/3.27
catual = money/5.10

print('Na cotação de 3.27, R${} só dá pra trocar para US${:.2f}'.format(money, c327))
print('Na cotação de 5.10, R${} só dá pra trocar para US${:.2f}'.format(money, catual))
