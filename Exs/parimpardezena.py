n = int(input('Informe um número inteiro'))
d = (n // 10) % 10 #lógica para pegar a dezena
if (d % 2==0): #verificando se a dezena é par,ímpar
    print("Primeiro número da dezena é PAR")
else:
    print("Primeiro número da dezena é ÍMPAR")