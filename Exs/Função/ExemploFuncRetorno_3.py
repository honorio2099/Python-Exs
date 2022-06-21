def soma(x,y):
    total = x + y
    if total > 9:
        return "Aprovado"
    else:
        return "Reprovado"
##################

#inicio do programa
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
s = soma(n1,n2)
print("Situação Final", s)