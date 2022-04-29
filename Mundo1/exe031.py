d = float(input('Digite a distância (em km) entre a origem e o destino de sua viagem: '))
if d <= 200:
    print('Sua viagem custará R$ {:.2f}'.format(d*0.5))
else:
    print('Sua viagem custará R$ {:.2f}'.format(d*0.45))
print('Boa viagem!')