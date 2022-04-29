import random

alunos = []
for i in range(4):
    alunos.append(str(input('Digite o nome do aluno: ')))

ordem_apresentação = alunos.copy()
random.shuffle(ordem_apresentação)
print('A ordem dos alunos que irão apresentar o trabalho será:')
for i in range(4):
    print('    {}º. {}'.format(i+1, ordem_apresentação[i]))