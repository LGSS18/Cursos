print('========== DESAFIO 013 ==========')
print('')

print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com x% de aumento.')
print('')

sal = float(input('Digite o salário: '))
por = float(input('Digite a porcentagem: '))
print('')

p = (sal * por)/100
sa = sal + p

print('O salario de R${} com um aumento de {}% fica com o total de R${:.2f}'.format(sal, por, sa))
