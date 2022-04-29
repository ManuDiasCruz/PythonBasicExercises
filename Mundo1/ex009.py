n = int(input('Digite um número na tela: '))
print('A tabuada de {} é: '.format(n))
for i in range(11):
    print('    {} x {:2} = {:2}'.format(n, i, n * i))