
while True:
    n = int(input("De qual número você quer a tabuada (digite um número negativo para parar)?"))
    if n<0:
        break
    print(f"{5*'-'}TABUADA DE {n}{5*'-'}")
    for i in range (0,11):
        print(f"{i}x{n}={i*n}")
