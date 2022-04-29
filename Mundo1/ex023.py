import os

n = int(input('Digite um número entre 0 e 9999 (incluídos): '))
if (n>9999) or (n<0):
    print('Número fora do intervalo!')
    n = int(input('Vou te dar uma chance...\nDigite um número entre 0 e 9999 (incluídos): '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O número {} tem:\n    - {} milhar(es)\n    - {} centena(s)\n    - {} dezena(s)\n    - {} unidade(s)'.format(n, m, c, d, u))