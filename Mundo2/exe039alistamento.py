from datetime import date

ano_nasc = int(input('Digite o ano em que você nasceu: '))
ano = date.today().year

if ano_nasc + 18 == ano:
    print('Está na hora de você se alistar no exército!')
elif ano_nasc + 18 >= ano:
    print('Você ainda é muito novo, ainda faltam {} anos para você poder se alistar.'.format((ano_nasc+18)-ano))
else:
    print('Se você nunca se alistou, está encrencado. Já faz {} anos que devia ter se alistado!'.format(ano-(ano_nasc+18)))