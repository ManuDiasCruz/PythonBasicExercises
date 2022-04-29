n = int(input("Digite um número: "))
resp = input("Quer continuar? [s/n] ")
total = 1
soma = n
maior = menor = n

while resp == 's':
    n = int(input("Digite um número: "))
    resp = input("Quer continuar? [s/n] ")
    total+=1
    soma+=n
    if n<menor:
        menor = n
    if n>maior:
        maior = n

print("Você digitou {} números, cuja média aritmética resoltou em {}.\nSendo {} o maior número e {} o menor número.".format(total, soma/total, maior, menor))