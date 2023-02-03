print('========== DESAFIO 012 ==========')
print('')

print('Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto.')
print('')

preco = float(input('Digite o preço do produto: '))
desconto = float(input('Digite o valor do desconto: '))
print('')

da = (preco * desconto)/100
pd = preco - da

print('O valor R${} com o desconto de {}% aplicado fica R${:.2f}'.format(preco, desconto, pd))
