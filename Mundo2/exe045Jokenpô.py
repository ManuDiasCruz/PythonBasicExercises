from time import sleep
from random import randint
import emoji

cor = {'limpar': '\033[m',
       'branco': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'anil': '\033[34m',
       'roxo': '\033[35m',
       'azul': '\033[36m'}

print('-'*44)
print('|{} Bem vindo ao jogo Jokenpô! {}|'.format(' '*7, ' '*7))
print('-'*44)
print('\n')

jogada = [['Pedra', ':fist_oncoming:'], ['Papel',':raised_hand_with_fingers_splayed:'], ['Tesoura', ':v:']]

print(emoji.emojize('Escolha sua jogada:'
      '\n    0 - Pedra   {}'
      '\n    1 - Papel   {}'
      '\n    2 - Tesoura {}'.format(jogada[0][1], jogada[1][1], jogada[2][1]), use_aliases=True))
print('Vou te dar 2 segundos para escolher, enquanto escolho a minha...')

computador = randint(0,2)
jogador = int(input('Qual sua jogada? '))

print('\nJO...')
sleep(1)
print('KEN...')
sleep(1)
print('PÔ!\n')
sleep(1)

if jogador < 0 or jogador > 2:
    print('{}Você escolheu uma jogada inválida!'.format(cor['anil']))
else:
    print('-' * 24)
    print(emoji.emojize('|    Computador: {}{}{}    |'.format(cor['amarelo'], jogada[computador][1], cor['limpar']), use_aliases=True))
    print(emoji.emojize('|    Jogador:    {}{}{}    |'.format(cor['amarelo'], jogada[jogador][1], cor['limpar']), use_aliases=True))
    print('-' * 24)
    print('\n')

    if jogada[computador][0] == jogada[jogador][0]:
        print('{}Empatamos!'.format(cor['amarelo']))
    elif (jogada[computador][0] == 'Papel' and jogada[jogador][0] == 'Pedra') or \
            (jogada[computador][0] == 'Tesoura' and jogada[jogador][0] == 'Papel') or \
            (jogada[computador][0] == 'Pedra' and jogada[jogador][0] == 'Tesoura'):
        print('{}Me desculpa, mas... você PERDEU e eu GANHEI!'.format(cor['vermelho']))
    else:
        print('{}Dessa vez você me pegou!\nPARABÉNS, você ganhou!'.format(cor['verde']))
