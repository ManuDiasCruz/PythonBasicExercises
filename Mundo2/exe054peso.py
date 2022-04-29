maior = 0.0
menor = 500.0

for i in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('Entre os pesos digitados o maior é {:.1f} e o menor é {:.1f}'.format(maior, menor))