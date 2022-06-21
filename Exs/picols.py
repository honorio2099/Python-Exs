print("================================================")
print("|           | SORVETES  DO  SEU ZÉ |           |")
print("|           |----------------------|           |")
print("|              OPÇÕES DE SORVETE:              |")
print("|   [1] - PICOLÉ DE CHOCOLATE                  |")
print("|   [2] - PICOLÉ DE MORANGO                    |")                          
print("|   [3] - PICOLÉ DE MILHO                      |")
print("|   [4] - SAIR DO SISTEMA                      |")
print("================================================")
def interface():
     print("================================================")
     print("|           | SORVETES  DO  SEU ZÉ |           |")
     print("|           |----------------------|           |")
     print("|              OPÇÕES DE SORVETE:              |")
     print("|   [1] - PICOLÉ DE CHOCOLATE                  |")
     print("|   [2] - PICOLÉ DE MORANGO                    |")                          
     print("|   [3] - PICOLÉ DE MILHO                      |")
     print("|   [4] - SAIR DO SISTEMA                      |")
     print("================================================")
option = int(input("Escolha Seu Picolé!!!(Ou Abandone o Sistema)"))
print()
qtdPic1 = 0
qtdPic2 = 0
qtdPic3 = 0
while option != 4:
     qtd = int(input("Digite a Quantidade de Picolés:"))
     if option == 1:
         qtdPic1 = qtdPic1 + qtd
     if option == 2:
         qtdPic2 = qtdPic2 + qtd
     if option == 3:
         qtdPic3 = qtdPic3 + qtd
     import os
     os.system('clear') or None
     interface()
     option = int(input("Faça sua Escolha!!! Picolés com Desconto! (Ou saia do Sistema)"))
totalpicoles = qtdPic1 + qtdPic2 + qtdPic3 
totalvendido = (qtdPic1*0.50) + (qtdPic2*0.60) + (qtdPic3*0.25)
import os
os.system('clear') or None
print("=======================================================")
print("A quantidade de picolés de Chocolate vendidos foi:",qtdPic1)
print("A quantidade de picolés de Morango vendidos foi:",qtdPic2)
print("A quantidade de picolés de Milho vendidos foi:",qtdPic3)
print("A quantidade Total de picolés vendidos foi:",totalpicoles)
print("A quantidade Total de lucro arrecadado foi: R$",totalvendido)
print("=======================================================")
