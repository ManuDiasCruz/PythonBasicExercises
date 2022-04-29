'''
# Alternativa 1: Importa apenas as funções que for usar, quanod for usar pode chmar direto a função como se ela fosse interna
from math import sqrt, ceil
n = int(input('Digite um número: '))
print('A raiz quadrada de {} é {:.3f}.'.format(n, ceil(sqrt(n))))

#Alternativa 2: Importa o módulo e quando for usar chama por um nome, no nosso caso mt e usa chamando esse nome
import math as mt
n = int(input('Digite um número: '))
print('A raiz quadrada de {} é {:.3f}.'.format(n, mt.ceil(mt.sqrt(n))))
'''

#Alternativa 2: Importa o módulo e quando for usar chama pelo nome do módulo
import math
n = int(input('Digite um número: '))
print('A raiz quadrada de {} é {:.3f}.'.format(n, math.ceil(math.sqrt(n))))
