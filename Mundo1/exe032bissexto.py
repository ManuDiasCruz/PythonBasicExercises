ano = int(input('Digite um ano: '))
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
print('O ano {} é bissexto.'.format(ano) if bissexto else 'O ano {} NÃO é bissexto.'.format(ano))
'''
if bissexto:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} NÃO é bissexto.'.format(ano))
'''