n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {0}, o produto é {1} e a divisão {2:.2f}'.format(s, m, d), end=' ')
print('A divisão inteira é {0} e potência é {1}'.format(di, e))
