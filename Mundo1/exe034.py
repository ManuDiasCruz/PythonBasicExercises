sal = float(input('Digite o valor do seu salário: '))
inc = sal * .15 if sal <= 1250 else sal * .1
'''
#Essa linha de cima resume o if else abaixo 
if sal <= 1250:
    inc = sal * .15
else:
    inc = sal * .1
'''
print('Você receberá um aumento de R$ {:.2f} e seu novo salário será R$ {:.2f}'.format(inc, sal+inc))