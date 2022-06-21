def soma(x,y):
    total = x + y
    sub  = x - y
    return total, sub
##################

#inicio do programa
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
s = soma(n1,n2)
print("Soma =", s[0])
print("Subtração =", s[1])
