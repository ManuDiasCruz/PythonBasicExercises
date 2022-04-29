from time import sleep
import emoji

c = int(input('Digite o tempo da contagem regressiva: '))

for i in range (c, -1, -1):
    print('{} '.format(i), end="")
    sleep(1)

print(emoji.emojize('\n:fireworks: :fireworks: :fireworks:', use_aliases=True))