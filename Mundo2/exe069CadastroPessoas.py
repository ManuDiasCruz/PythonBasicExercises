maioridade = homens = mAbaixoDe20 = cont = 0

while True:
    print(30 * "-")
    print(f"{5 * ' '}CADASTRO DE PESSOAS{5 * ' '}")
    print(30 * "-")
    idade=int(input("Idade: "))
    while idade<0:
        idade = int(input("Idade: "))

    sexo=input("Sexo (M/F):")
    while sexo.upper()!='M' and sexo.upper()!='F':
        sexo=input("Sexo (M/F):")

    if idade >= 18:
        maioridade+=1
    if sexo.upper() == 'M':
        homens+=1
    if sexo.upper() =='F' and idade<20:
        mAbaixoDe20+=1;

    cont+=1

    cadastra = input("Quer continuar? (S/N) ")
    if cadastra.upper() == 'N':
        break
    while cadastra.upper() != 'S' and cadastra.upper() != 'N':
        cadastra = input("Quer continuar? (S/N) ")

print(f"{7*'='}FIM DO PROGRAMA{7*'='}")
print(f"Foram cadastradas {cont} pessoas.")
print(f"Dentre elas:")
print(f"    {maioridade} tem mais de 18 anos.")
print(f"    {homens} são homens.")
print(f"    {mAbaixoDe20} são mulheres com menos de 20 anos.")
