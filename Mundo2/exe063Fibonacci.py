n = int(input("Digite quantos termos de Fibonacci vocês quer ver: "))

#Primeiros termos da sequência por definição
t1 = 0
t2 = 1

print("A sequência de Fibonacci é:")
print("{}, {}".format(t1, t2), end='')
i = 1
while i<=n-2:
    t = t1 + t2
    print(", {}".format(t), end='')
    t1 = t2
    t2 = t
    i+=1