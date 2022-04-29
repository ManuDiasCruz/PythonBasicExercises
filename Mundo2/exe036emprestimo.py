cor = {'limpar': '\033[m',
       'branco': '\033[30m',
       'vermelho': '\033[31m',
       'verde': '\033[32m',
       'amarelo': '\033[33m',
       'anil': '\033[34m',
       'roxo': '\033[35m',
       'azul': '\033[36m'}

print('{} Bem vindo a nossa simulação de empréstimo da sua casa nova! {}'.format('-'*10, '-'*10))
casa = float(input('Digite o valor da casa que você deseja comprar? R$ '))
salario = float(input('Qual seu salário atual? R$ '))
prazo = 12* int(input('Em quantos anos deseja financiar o imóvel? '))

mensalidade = casa/prazo
if mensalidade <= salario*.3:
    print('{}PARABÉNS, você conseguirá o empréstimo.{}\nO valor da sua prestção mensal será de R$ {:.2f}'.format(cor['verde'], cor['limpar'], mensalidade))
else:
    print('Seu empréstimo foi {}NEGADO!{}\nCom o seu salário atual você não poderá financiar este imóvel no tempo que deseja.'.format(cor['vermelho'], cor['limpar']))