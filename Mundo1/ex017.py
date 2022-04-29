from math import pow, sqrt, hypot
co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))
print('O valor da hipotenusa do triângulo retânculo com cateto oposto {}u. e cateto adjacente {}u. é {:.2f}u..'
      .format(co, ca, sqrt(pow(co, 2)+pow(ca, 2))))
                      #hypot(ca, co)))