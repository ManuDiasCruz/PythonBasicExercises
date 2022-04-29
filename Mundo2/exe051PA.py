pt = int(input('Digite o primeiro termo de sua Progressão Aritmética (PA): '))
r = int(input('Digite a razão de sua PA: '))

print('Os 10 primeiros termos de sua PA são: ')
for i in range(pt, pt+(r*10), r):
    print("{}, ".format(i), end='')