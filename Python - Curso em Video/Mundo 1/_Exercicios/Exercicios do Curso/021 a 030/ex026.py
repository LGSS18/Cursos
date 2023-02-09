print('========== DESAFIO 026 ==========')
print('')

print('Faça um programa que leia uma frase pelo teclado e mostre:')
print('1 - Quantas vezes aparece a letra "A".')
print('2 - Em que posição ela aparece a primeira vez.')
print('3 - Em que posição ela aparece a última vez.')
print('')

frase = input('Digite a frase: ')
print('')

print('1 - {}'.format(frase.lower().count('a')))
print('2 - {}'.format(frase.lower().find('a')))
print('3 - {}'.format(frase.lower().rfind('a')))
