n = int(input('Digite um número: '))

ehPrimo = True

for i in range(2, n):
    if n % i == 0:
        ehPrimo = False

print('O número {} que você escolheu é primo? {}'.format(n, ehPrimo))