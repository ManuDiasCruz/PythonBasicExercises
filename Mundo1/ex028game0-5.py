from random import randint
from time import sleep

cor = {'limpar': '\033[m',
       'branco': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'anil': '\033[34m',
       'roxo': '\033[35m',
       'azul': '\033[36m'}

print('{}'.format('\033[7;35;40m'))
print('-'*50)
print('|{} Bem vindo ao jogo da advinhação! {}|'.format(' '*7, ' '*7))
print('-'*50)
print('Vou pensar em um número entre 0 e 5. Será que você consegue advinhar?!')
print('Pensando...')
np = randint(0, 5)
sleep(3)
n = int(input('Já pensei!\n\nTente advinhar! Qual número eu pensei? '))

if n == np:
    print('PARABÉNS!!! Você acertou')
else:
    print('0x1 para mim amigo. Você errou! Eu tinha pensado no número {}.'.format(np))