soma = acima1000 = barato = cont = 0
nomeBarato = ""

while True:
    print(30 * "-")
    print(f"{8 * ' '}SUPER LOJÃO{8 * ' '}")
    print(30 * "-")
    produto=input("Nome do produto: ")
    while len(produto)<1:
        produto = input("Nome do produto: ")

    preco = float(input("Preço: "))
    while preco < 0:
        preco = float(input("Preço: "))

    soma+=preco
    if preco >= 1000:
        acima1000+=1

    if cont==0:
        barato=preco
        nomeBarato=produto
    else:
        if preco < barato:
            barato = preco
            nomeBarato = produto

    cont += 1

    cadastra = input("Quer continuar? (S/N) ")
    if cadastra.upper() == 'N':
        break
    while cadastra.upper() != 'S' and cadastra.upper() != 'N':
        cadastra = input("Quer continuar? (S/N) ")


print(f"{7*'='}FIM DA COMPRA{7*'='}")
print(f"valor final da compra: R$ {soma:,.2f}")
print(f"Quantidade de itens: {cont}.")
print(f"O produto mais barato foi {nomeBarato} que custou R$ {barato:,.2f}.")
print(f"{acima1000} custam mais que R$ 1.000,00.")