n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua média é {:0.1f}.'.format(m))
print('Sua média foi boa! PARABÉNS!' if m >=7 else 'Sua média foi ruim. ESTUDE MAIS!')
'''
if m>= 7:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim. ESTUDE MAIS!')
'''
print('Boa sorte!')
