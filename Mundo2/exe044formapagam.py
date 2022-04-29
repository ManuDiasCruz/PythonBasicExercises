preco = float(input('Digite o preço do produto: R$ '))
print('Nossas formas de pagamento são:'
      '\n    1 - Á vista no dinheiro/cheque, desconto de 10%'
      '\n    2 - Á vista no cartão, desconto de 5%'
      '\n    3 - Em até 2x no cartão'
      '\n    4 - A partir de 3x no cartão, juros de 20%')
forma_pag = int(input('Digite o número correspondente a opção que deseja pagar: '))
preco_final = 0.0

if forma_pag == 1:
    preco_final = preco * .9
elif forma_pag == 2:
    preco_final = preco * .95
elif forma_pag == 3:
    preco_final = preco
elif forma_pag == 4:
    preco_final = preco * 1.2
else:
    preco_final = -1

print('O preço final do seu produto será de R$ {:.2f}'.format(preco_final) if preco_final != -1 else 'Você não selecionou nenhuma forma de pagamento.')