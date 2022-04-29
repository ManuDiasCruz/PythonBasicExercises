from datetime import date

ano = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))
categorias = ['MIRIM', 'INFANTIL', 'JUNIOR', 'SÊNIOR', 'MASTER']

idade = ano -  nasc

if idade < 9:
    print('A categoria do atleta é {}.'.format(categorias[0]))
elif idade < 14:
    print('A categoria do atleta é {}.'.format(categorias[1]))
elif idade < 19:
    print('A categoria do atleta é {}.'.format(categorias[2]))
elif idade < 20:
    print('A categoria do atleta é {}.'.format(categorias[3]))
else:
    print('A categoria do atleta é {}.'.format(categorias[4]))