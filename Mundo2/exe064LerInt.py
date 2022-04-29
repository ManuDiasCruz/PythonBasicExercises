total = soma = 0

n = int(input("Digite um número inteiro (999 para parar): "))

while n != 999:
    total += 1
    soma += n
    n = int(input("Digite um número inteiro (999 para parar): "))

print("VOcê digitou um total de {} números cuja soma é {}.".format(total, soma))