print('Os números ímpares múltiplos de 3 no intervalo de {} a {} são: '.format(1, 500))

c = 0
soma = 0
for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        print('{} '.format(i), end='')
        c = c+1
        soma = soma + i

print('\nNeste intervalo foram encontrados {} números que satisfazem a condição e sua soma é {}.'.format(c, soma))