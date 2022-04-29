ns = []
ns.append(int(input('Digite um número: ')))
ns.append(int(input('Digite outro número: ')))
ns.append(int(input('Digite o último número: ')))
ls = ns.copy()
ls.sort()

print('Considerando os números que vocês digitou {}. O maior é {} e o menor é {}.'.format(ns, ls[-1], ls[0]))