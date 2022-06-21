def matrizEscada():
    matriz = []
    linha = 5
    coluna = 1
    n = int(input("Digite um número:"))
    for i in range(1,n+1):
        lin = [] #criando uma nova lista
        j = 1
        while j <= coluna:
            lin.append(i) #preenchendo com os números
            j += 1
        matriz.append(lin)
        coluna += 1
    for linhaMat in matriz:
        print(linhaMat)
matrizEscada()



    

