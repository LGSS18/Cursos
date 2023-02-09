print('==========')
print('')
frase = 'Curso em Video Python'

print(frase)
print('')

print('--- Fatiamento ---')

print(frase[:5])
print(frase[9:14])
print(frase[15:])

print(frase[0:14:2])
print(frase[0::2])

print('')
print('--- Análise ---')

print(len(frase))
print(frase.count('o'))
print(frase.count('e', 0, 14))
print(frase.find('Video'))
print('Curso' in frase)

print('')
print('--- Transformação ---')

print(frase.replace('Python', 'C#'))
print(frase.replace(' ', ''))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.replace('Curso em ', '   Aprenda '))
frase2 = '   Aprenda Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

print('')
print('--- Divisão ---')
print(frase.split())
print('-'.join(frase))
dividido = frase.split()
print(dividido[0])
print(dividido[1])
print(dividido[2])
print(dividido[3])
print(dividido[3][1])


print('')
print('==========')
