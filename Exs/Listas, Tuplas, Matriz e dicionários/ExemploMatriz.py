matriz = []
linha = 5
coluna = 5
for i in range(linha):
    lin = [] #criando uma nova lista
    for j in range(coluna):
        cont = i+j
        lin.append(cont) #preenchendo com os números
    matriz.append(lin)

print("Matriz =>", matriz)
print("Item da matriz =>", matriz[1][2])

for linhaMat in matriz:
    print(linhaMat)

    

