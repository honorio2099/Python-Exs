def soma(x,y):
    total = x + y
    print("Total da função da soma =", total)
##################

#inicio do programa
global total
total = 10
print("Total da variável do programa principal antes da função =", total)
soma(3,5)
print("Total da variável do programa principal depois da função=", total)
