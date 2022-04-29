import datetime

ano = int(input('Qual o ano do seu carro? '))
ano_atual = int(datetime.datetime.now().date().strftime('%Y'))
#ano_atual = datetime.date().today().year #Alternativa a linha acima para pegar o ano e já retorna em int
if (ano_atual-ano)<=3:
    print('Seu carro é bem novo, tem apenas {} ano(s).'.format(ano_atual-ano))
else:
    print('Seu carro tem mais de 3 anos, logo não é novo.')