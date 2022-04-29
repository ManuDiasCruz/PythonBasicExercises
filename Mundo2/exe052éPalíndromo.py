frase = input('Digite uma frase: \n').strip().replace(' ', '').upper()

tf = len(frase)
cont = 0

for i in range(0, (tf//2)+1):
    print(tf-i-1)
    if frase[i] != frase[tf-i-1]:
        cont = cont + 1

print('A frase que você digitou é um palíndromo? {}'.format(False if cont > 0 else True))