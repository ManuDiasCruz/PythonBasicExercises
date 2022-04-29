frase = input('Digite uma frase: \n').strip().upper()
pi = frase.find('A') + 1
pf = len(frase) - (''.join(reversed(frase)).find('A')) # frase.rfind('A') +1
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
if frase.count('A') > 0:
    print('A primeira vez que aparece a letra A aparece na frase é na {}ª posição e a última é na {}ª posição.'.format(pi, pf))