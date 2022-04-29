from datetime import date

maiores = 0
menores = 0
for i in range(0, 7):
    nascimento = int(input('Digite o ano em que você nasceu: '))
    if date.today().year - nascimento >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1

print('Entre as pessoas que responderam ao questionários {} são maiores de idade (>= 18 anos) e {} são menores de idade.'.format(maiores, menores))