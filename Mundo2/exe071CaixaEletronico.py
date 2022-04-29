print(29 * ":")
print(f"{10 * ' '}BANCO CEV{10 * ' '}")
print(29 * ":")
saque=int(input("Qual valor deseja sacar? R$ "))

ced50 = saque//50
saque -= ced50 * 50

ced20 = saque//20
saque -= ced20 * 20

ced10 = saque//10
saque -= ced10 * 10

print("Contagem de células:")
if (ced50>0):
    print(f"  {ced50} cédulas de R$ 50.00")
if (ced20>0):
    print(f"  {ced20} cédulas de R$ 20.00")
if (ced10>0):
    print(f"  {ced10} cédulas de R$ 10.00")
if (saque>0):
    print(f"  {saque} cédulas de R$ 1.00")

print(f"Nº total de cédulas: {ced50+ced20+ced10+saque}.")
print(29 * ".")

print("Volte sempre ao banco CEV!")
print("Tenha um bom dia.")
# Cédulas 50, 20, 10 e 1