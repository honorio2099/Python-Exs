totalP1 = 0
totalP2 = 0
totalP3 = 0
totalP4 = 0
totalP5 = 0
totalP6 = 0
totalR = 0
valor = 0
media = 0
pedidos = 0
pgmto = 0
print("=========================================================")
print("    | CÓDIGO |    |> PRODUTOS <|   | PREÇO UNITÁRIO (R$)|")
print("--------------------------------------------------------")
print("    |    1    |   | CAMISETA B |   |R$      7,00        |")
print("    |    2    |   | CAMISETA C |   |R$      9,00        |")
print("    |    3    |   | MOLETON    |   |R$     17,00        |")
print("    |    4    |   | CALÇA      |   |R$     12,00        |")
print("    |    5    |   | ABRIGO     |   |R$     25,00        |")
print("    |    6    |   | BONÉ       |   |R$      5,00        |")
print("=========================================================")
option = int(input("Por Favor informe o código do produto escolhido:"))
qtd = int(input("Por favor informe a quantidade que deseja:"))
option2 = ''
while pedidos != 10:
    if (option == 1):
        totalP1 += qtd
        valor = 7.00
        totalR += valor * qtd
        pgmto = valor * qtd
        print("O total a pagar é:",pgmto)
        option2 = input('Deseja Continuar? [sim] ou [não]')
    elif (option2 == 'não'):
        break
    if (option == 2):
        totalP2 += qtd
        valor = 9.00
        totalR += valor * qtd
        pgmto = valor * qtd
        print("O total a pagar é:",pgmto)
        option2 = input('Deseja Continuar? [sim] ou [não]')
    elif (option2 == 'não'):
        break
    if (option == 3):
        totalP3 += qtd
        valor = 17.00
        totalR += valor * qtd
        pgmto = valor * qtd
        print("O total a pagar é:",pgmto)
        option2 = input('Deseja Continuar? [sim] ou [não]')
    elif (option2 == 'não'):
        break
    if (option == 4):
        totalP4 += qtd
        valor = 12.00
        totalR += valor * qtd
        pgmto = valor * qtd
        print("O total a pagar é:",pgmto)
        option2 = input('Deseja Continuar? [sim] ou [não]')
    elif (option2 == 'não'):
        break
    if (option == 5):
        totalP5 += qtd
        valor = 25.00
        totalR += valor * qtd
        pgmto = valor * qtd
        print("O total a pagar é:",pgmto)
        option2 = input('Deseja Continuar? [sim] ou [não]')
    elif (option2 == 'não'):
        break
    if (option == 6):
        totalP6 += qtd
        valor = 5.00
        totalR += valor * qtd
        pgmto = valor * qtd
        print("O total a pagar é:",pgmto)
        option2 = input('Deseja Continuar? [sim] ou [não]')
    elif (option2 == 'não'):
        break
    import os
    os.system('clear')
    print("=========================================================")
    print("    | CÓDIGO |    |> PRODUTOS <|   | PREÇO UNITÁRIO (R$)|")
    print("--------------------------------------------------------")
    print("    |    1    |   | CAMISETA B |   |R$      7,00        |")
    print("    |    2    |   | CAMISETA C |   |R$      9,00        |")
    print("    |    3    |   | MOLETON    |   |R$     17,00        |")
    print("    |    4    |   | CALÇA      |   |R$     12,00        |")
    print("    |    5    |   | ABRIGO     |   |R$     25,00        |")
    print("    |    6    |   | BONÉ       |   |R$      5,00        |")
    print("=========================================================")
    option = int(input("Por Favor informe o código do produto escolhido:"))
    qtd = int(input("Por favor informe a quantidade que deseja:"))
totalP = totalP1 + totalP2 + totalP3 + totalP4 + totalP5 + totalP6
media = totalR/totalP
print("===================================================")
print("| Total vendido de Camiseta Branca:",totalP1,"  |")
print("| Total vendido de Camiseta Colorida:",totalP2,"|")
print("| Total vendido de Moleton:",totalP3,"          |")
print("| Total vendido de Calça:",totalP4,"            |")
print("| Total vendido de Abrigo:",totalP5,"           |")
print("| Total vendido de Boné:",totalP6,"             |")
print("| Total de produtos vendidos:",totalP,"         |")
print("| Total arrecadado:",totalR,"                   |")
print("| Valor médio:",media,"                         |")
print("====================================================")
        
        
        
        
        
        