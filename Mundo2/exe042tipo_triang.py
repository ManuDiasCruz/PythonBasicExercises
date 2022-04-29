r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

tr1 = abs(r2-r3) < r1 < r2+r3
tr2 = abs(r1-r3) < r2 < r1+r3
tr3 = abs(r1-r2) < r3 < r1+r2

if tr1 and tr2 and tr3:
    if r1 == r2 == r3:
        print('Com as retas de tamanhos {}, {} e {} é possível formar um triâgulo equilátero.'.format(r1, r2, r3))
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Com as retas de tamanhos {}, {} e {} é possível formar um triâgulo isósceles.'.format(r1, r2, r3))
    else:
        print('Com as retas de tamanhos {}, {} e {} é possível formar um triâgulo escaleno.'.format(r1, r2, r3))
else:
    print('As retas com os tamanhos que você forneceu não formam um triângulo.')