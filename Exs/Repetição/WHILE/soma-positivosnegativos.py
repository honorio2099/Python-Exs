cont = 0
soma = 0
media = 0
negativo = 0
while cont != 5:
    n = int(input("Digite um número:"))
    if n > 0:
    soma += n
    positivos += 1
    if n < 0:
       negativo += 1 
    cont += 1
media = soma/positivos
print("A soma dos números é:",soma)
print("Os negativos são:",negativo)
print("A média é:",media)
    