from random import randint

print(31*"-")
print(f"|{6*' '}JOGO PAR OU ÍMPAR{6*' '}|")
print(31*"-")

cont = 0;
while True:
    jog = int(input("Escolha um número: "))
    escJog = input("Escolhar Par ou Ímpar (P/I):")

    pc = randint(0,10)

    if (jog+pc)%2 == 0 and escJog.upper() == 'P':
        print(f"Você jogou {jog} e o computador jogou {pc}.")
        print(f"{jog+pc} é par. Você ganhou!")

        cont+=1;
    elif (jog+pc)%2 != 0 and escJog.upper() == 'I':
        print(f"Você jogou {jog} e o computador jogou {pc}.")
        print(f"{jog+pc} é ímpar. Você ganhou!")

        cont+=1;
    else:
        print(f"Você jogou {jog} e o computador jogou {pc}.")
        if escJog.upper() == 'P':
            print(f"{jog + pc} é ímpar. Você perdeu!")
        else:
            print(f"{jog + pc} é par. Você perdeu!")
        print(31 * ".")
        break;

    print(31 * ".")

print(f"GAME OVER! Você venceu {cont} vezes.")

