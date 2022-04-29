diária = 60
quilômetro = 0.15
dias = int(input('O carro ficou alugado por quantos dias? '))
km = float(input('Quantos quilômetros o carro rodou (em km)? '))
diárias = diária*dias
km_rodados = quilômetro * km
print('O pagamento por diárias será {} dias x R$ {:.2f} que é igual a R$ {:.2f}.'.format(dias, diária, diárias))
print('O pagamento por quilômetros rodados será {}km x R$ {:.2f} que é R$ {:.2f}.'.format(km, quilômetro, km_rodados))
print('    R$ {:.2f} preço por diárias'.format(diárias))
print('+   R$ {:.2f} preço por km rodado'.format(km_rodados))
print('-' * 50)
print('    R$ {:.2f} é o total devido pelo aluguel!'.format(diárias + km_rodados))