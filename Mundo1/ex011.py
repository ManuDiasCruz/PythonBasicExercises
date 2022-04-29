alt = float(input('Qual a altura da sua parede (em metros)? '))
larg = float(input('Qual a largura de sua parede (em metros)? '))
print('A área de sua parede é {:.2f}m² e você precisará de pelo menos {:.2f}l de tinta para pintá-la.'.format(alt * larg, (alt * larg) / 2))