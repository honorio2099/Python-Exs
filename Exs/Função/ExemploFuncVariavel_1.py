def soma(x,y):
    global total
    total = x + y
    print("Total da função da soma =", total)
##################

#inicio do programa
total = 10
print("Total da variável do programa principal antes da função =", total)
soma(3,5)
print("Total da variável do programa principal depois da função=", total)
