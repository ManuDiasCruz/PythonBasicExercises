cor = {'limpar': '\033[m',
       'branco': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'anil': '\033[34m',
       'roxo': '\033[35m',
       'azul': '\033[36m'}

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

m = (n1+n2)/2

if m < 5:
    print('Sua média foi {:.1f}, logo você está {}REPROVADO'.format(m, cor['vermelho']))
elif m >= 7:
    print('Parabéns, você foi {}APROVADO{}! Seus estudos refletiram na sua média de {:.1f}.'.format(cor['verde'], cor['limpar'], m))
else:
    print('Com a média de {:.1f} você está de {}RECUPERAÇÃO!'.format(m, cor['amarelo']))