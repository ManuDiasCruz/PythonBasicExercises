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
    else:
        print(", PAUSA ")
j = 0
q = int(input('Quantos termos você quer mostrar a mais (use 0 para parar): '))
c=0
total = 10 + q
while q!=0 and j<q:
    print("{}".format(i), end='')
    i+=r
    c+=1
    if c<q:
        print(", ", end='')
    else:
        print(", PAUSA ")
        q = int(input('Quantos termos você quer mostrar a mais (use 0 para parar): '))
        total += q
        c=0
        j=0
print("A progressão foi finalizada com {} termos na tela.".format(total))
print("Tchau!")