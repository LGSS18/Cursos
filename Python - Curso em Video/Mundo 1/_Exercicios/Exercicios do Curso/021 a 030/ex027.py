print('========== DESAFIO 027 ==========')
print('')

print('Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.')
print('')

nome = input('Digite o seu nome: ')
print('')

print('Primeiro nome: {}'.format(nome.split()[0]))
print('Ultimo nome: {}'.format(nome.rsplit()[-1]))
