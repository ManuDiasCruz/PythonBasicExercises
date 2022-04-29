tabela = {18.5:'Abaixo do peso',
          25:'Peso ideal',
          30:'Sobrepeso',
          40:'Obesidade',
          41:'Obesidade mórbida'}

peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em m: '))

imc = peso / (altura*altura)
clas = '.'

if imc < 18.5:
    clas = clas.replace('.', tabela[18.5])
elif imc < 25:
    clas = clas.replace('.', tabela[25])
elif imc < 30:
    clas = clas.replace('.', tabela[30])
elif imc < 40:
    clas = clas.replace('.', tabela[40])
else:
    clas = clas.replace('.', tabela[41])

print('Com o peso {:.1f} Kg e a altura {:.2f} m, seu imc é {:.1f} e você está na faixa \'{}\'.'.format(peso, altura, imc, clas))
