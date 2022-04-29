v = int(input('Digite a velocidade do seu carro (em km/h): '))
cor = {'limpar': '\033[m',
       'branco': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'anil': '\033[34m',
       'roxo': '\033[35m',
       'azul': '\033[36m'}
if v > 80:
    print('{}A velocidade {}km/h está acima do permitido! Você será multado em R$ {},00.{}'.format(cor['vermelho'], v, (v-80)*7, cor['limpar']))
else:
    print('{}PARABÉNS! Você está dentro do limite de 80km/h.{}'.format(cor['verde'], cor['limpar']))