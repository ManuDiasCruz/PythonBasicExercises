n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))

print('O que vocês quer fazer com os números {} e {}?'.format(n1, n2))
print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
op = int(input('Digite uma opção entre as 5 acima:'))

while op != 5:
    if op == 1:
        print('A soma de {} e {} é {}.'.format(n1, n2, n1+n2))
    elif op == 2:
        print('A multiplicação de {} e {} é {}.'.format(n1, n2, n1*n2))
    elif op == 3:
        print('O maior entre os 2 números é {}.'.format(n1) if n1>n2 else 'O maior entre os 2 números é {}.'.format(n2))
    elif op == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

    print('E agora, o que gostaria de fazer?\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    op = int(input('Digite uma opção entre as 5 acima:'))

print('O programa foi encerrado!')