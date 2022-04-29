temp = float(input('Digite a temperatura em ºC: '))
print('A temperatura {:.1f}ºC equivale a {:.1f}ºF e {:.1f}K.'.format(temp, (temp*9/5)+32, temp + 273.15))