print('========== DESAFIO 033 ==========')
print('')

print('Faça um programa que leia três números e mostre qual é o maior e qual é o menor.')
print('')

n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o Segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 < n2 and n1 < n3:
    print('\nO menor número é {}'.format(n1))
    if n2 < n3:
        print('\nO maior número é {}'.format(n3))
    else:
        print('\nO maior número é {}'.format(n2))

if n2 < n1 and n2 < n3:
    print('\nO menor número é {}'.format(n2))
    if n1 < n3:
        print('\nO maior número é {}'.format(n3))
    else:
        print('\nO maior número é {}'.format(n1))

if n3 < n1 and n3 < n2:
    print('\nO menor número é {}'.format(n3))
    if n1 < n2:
        print('\nO maior número é {}'.format(n2))
    else:
        print('\nO maior número é {}'.format(n1))