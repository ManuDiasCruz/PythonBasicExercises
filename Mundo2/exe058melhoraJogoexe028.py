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
print('Vou pensar em um número entre 0 e 10. Será que você consegue advinhar?!')
print('Pensando...')
np = randint(0, 10)
sleep(3)
n = int(input('Já pensei!\n\nTente advinhar! Qual número eu pensei? '))
cont=0;
while n != np:
    cont+=1
    n = int(input('Você errou! Tente novamente... Qual número eu pensei? '))

if cont==0:
    print('PARABÉNS!!! Você acertou de primeira!')
else:
    print('Após {} tentativas, finalmente você acertou. Vamos tentar melhorar na próxima!'.format(cont))

