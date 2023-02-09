import random
print('========== DESAFIO 020 ==========')
print('')

print('O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos e mostre a ordem.')
print('')

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
print('')

lista = [aluno1, aluno2, aluno3, aluno4]
print(lista)
print('')
random.shuffle(lista)

print('A ordem será: {}'.format(lista))
