n = int(input("Digite um número: "))
'''i=1;
result = n
while i<n:
     result = result*i;
     i+=1'''
result=1
for i in range (1, n+1):
     result*=i

print('O fatorial de {} (na notação matemática {}!) é {}.'.format(n, n, result))