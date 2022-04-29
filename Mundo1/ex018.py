import math
ângulo = float(input('Digite um ângulo em º:'))
ar = math.radians(ângulo)
print('O ângulo {}º tem como valor de:\n - seno {:.2f}\n - cosseno {:.2f}\n - tangente {:.2f}'.format(ângulo, math.sin(ar), math.cos(ar), math.tan(ar)))