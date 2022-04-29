pt = int(input('Digite o primeiro termo de sua Progressão Aritmética (PA): '))
r = int(input('Digite a razão de sua PA: '))

print('Os 10 primeiros termos de sua PA são: ')
i=pt
c=0
while i<pt+(r*10):
    print("{}".format(i), end='')
    i+=r
    c+=1
    if c<10:
        print(", ", end='')