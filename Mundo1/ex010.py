dolar = 5.56
dinheiro = float(input('Quantos reais você tem na carteira? R$ '))
print('Se fosse comprar dólares hoje cuja cotação é US$ 1 = R$ {:.2f}, seu dinheiro R$ {:.2f} '
      'compraria apenas US${:.2f}.'.format(dolar, dinheiro, dinheiro /dolar))