nome = input('Digite seu nome completo: ').upper()
silva = nome.find('SILVA') > -1
print('Que legal, você também é da minha família Silva!' if silva == True else 'Você não tem Silva como sobrenome!')