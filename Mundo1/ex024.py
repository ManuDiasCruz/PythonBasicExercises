cidade = input('Digite o nome de uma cidade: ')
c = cidade.strip().upper()
valor = c[:5] == 'SANTO'
'''
cidade = input('Digite o nome de uma cidade: ').strip()
valor = c[:5].upper() == 'SANTO'
'''

print('O nome da cidade começa com o nome Santo? {}'.format(valor))