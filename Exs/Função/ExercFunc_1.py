def inverter(num):
    qtdCar = len(num)       #contar a qtd de caracteres
    print("qtd de caracteres", qtdCar)
    numInv = ""             #acumuladora do tipo string que será inicializada com vazio
    i = (qtdCar - 1)        #len conta de 1, mas os indices da STRING começam em 0
    while i >= 0:
        numInv = numInv + num[i]
        i = i - 1
    print(num,"invertendo é", numInv)
###################

#programa principal
n = input("Digite o n")
inverter(n)