cont = 0
divisivel = 0
while cont != 5:
    n = int(input("Digite um número:"))
    if n%3==0:
        divisivel += 1
    cont += 1
print("A quantidade de Contadores divisíveis por 3 é:",divisivel)
    