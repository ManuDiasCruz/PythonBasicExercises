msg = input('Digite algo: ')
print('O tipo primitivo dessa entrada é {}'.format(type(msg)))
print('Só tem espaços? {}'.format(msg.isspace()))
print('É um número? {}'.format(msg.isnumeric()))
print('É alfabético? {}'.format(msg.isalpha()))
print('É alafanumérico? {}'.format(msg.isalnum()))
print('Está só em maiúscula? {}'.format(msg.isupper()))
print('Está só em minúscula? {}'.format(msg.islower()))
print('Está \'capitalizada \'? {}'.format(msg.istitle()))