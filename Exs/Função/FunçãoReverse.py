def reverso(contrario):
    contrario.reverse()  
    return contrario
cont = 0
n = []
while cont != 3:
    num = [input('Digite um número inteiro:')]
    n.append(num)
    cont+=1
c = reverso(n)
print("O seu número ao contrário é:",c[0],c[1],c[2])