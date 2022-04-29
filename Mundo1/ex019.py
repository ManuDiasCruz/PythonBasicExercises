import random

alunos = []
for i in range(4):
    alunos.append(str(input('Digite o nome do aluno: ')))

print('O aluno escolhido é {}.'.format(random.choice(alunos)))
