números = []
soma = 0
for i in range(0, 6):
    números.append(int(input('Digite um número: ')))
    if números[i] % 2 == 0:
        soma = soma + números[i]

print('A soma dos valores pares da lista {} é {}.'.format(números, soma))