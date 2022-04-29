pessoas = []
soma_idades = 0
mais_velho = -1
mulheres_menor_idade = 0
for i in range(0, 4):
    nome = input('Digite seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Você é do sexo masculino ou Feminino? ').strip().lower()
    pessoas.append([nome, idade, sexo])

    soma_idades = soma_idades + idade
    if sexo == 'masculino' and idade > mais_velho:
        mais_velho = idade
        quem_eh_mais_velho = i
    if sexo == 'feminino' and idade < 21:
        mulheres_menor_idade = mulheres_menor_idade + 1

    print('\n')

media_idades = soma_idades/4

print('Segundo nosso banco de dados:')
print('    - A média das idades é {:.2f} anos.'.format(media_idades))
print('    - O nome do homem mais velho é {}.'.format(pessoas[quem_eh_mais_velho][0]))
print('    - Existem {} mulhere(s) com menos de 21 anos.'.format(mulheres_menor_idade))
