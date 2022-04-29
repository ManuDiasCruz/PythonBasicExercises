print('Os números pares no intervalo de {} a {} são: '.format(1, 50))

c = 0
for i in range(1, 51):
    if i % 2 == 0:
        print('{} '.format(i), end='')
        c = c+1

print('\nNeste intervalo foram encontrados {} números pares.'.format(c))