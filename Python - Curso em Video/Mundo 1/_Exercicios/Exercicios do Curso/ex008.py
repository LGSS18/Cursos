print('========== DESAFIO 008 ==========')
print('')

print('Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.')
print('')

vm = float(input('Digite um valor em metro: '))
print('')

vcm = vm * 100
vmm = vm * 1000

print('O valor de {}m em cm é: {}'.format(vm, vcm))
print('O valor de {}m em mm é: {}'.format(vm, vmm))
