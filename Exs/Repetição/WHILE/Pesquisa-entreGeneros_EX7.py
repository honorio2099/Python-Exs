maioridadeM = 0
maioridadeF = 0
idade = 0
sexoM = 0
sexoF = 0
salM = 0
somasalM = 0
somasalF = 0
salF = 0
salFmaiorC = 0
mediaSalM = 0
mediaSalF = 0
print("===================================================")
print("|>  PESQUISA dos integrantes do instituto GO-IT  <|")
print("|-------------------------------------------------|")
print("| Para sair, digite uma idade negativa no sistema |")
print("===================================================")
idade = int(input("Por favor informe a sua idade:"))
option = input("Por Favor informe seu Sexo: [M] ou [F]")
sal = float(input('Digite seu salário:'))
menoridadeM = idade
menoridadeF = idade
while idade > 0:
    if idade <= 0:
        break
        if (option == "M"):
            sexoM += 1
            salM = sal
            somasalM += salM
            mediaSalM = somasalM/sexoM
            if idade > maioridadeM:
            maioridadeM = idade 
            if idade < menoridadeM:
            menoridadeM = idade
        if (option == "F"):
            sexoF += 1
            salF = sal
            somasalF += salF
            mediaSalF = somasalF/sexoF
            if idade > maioridadeF:
            maioridadeF = idade 
            if idade < menoridadeF:
            menoridadeF = idade
        if salF > 0 and salF < 100:
            salFmaiorC += 1
    import os
    os.system('clear')
    print("===================================================")
    print("|>  PESQUISA dos integrantes do instituto GO-IT  <|")
    print("|-------------------------------------------------|")
    print("| Para sair, digite uma idade negativa no sistema |")
    print("===================================================")
    idade = int(input("Por favor informe a sua idade:"))
    option = input("Por Favor informe seu Sexo: [M] ou [F]")
    sal = float(input('Digite seu salário:'))

print("=============================================")
print("Informações do genêro masculino -")
print("A maior idade masculina é:",maioridadeM,"   |")
print("A menor idade masculina é:",menoridadeM,"   |")
print("A média do salário masculino é:",mediaSalM,"|")
print("====================================================")
print("Informações do genêro feminino -")
print("A maior idade feminina é:",maioridadeF,"           |")
print("A menor idade feminina é:",menoridadeF,"           |")
print("A média de salário feminina é:",mediaSalF,"        |")
print("Mulheres com salário entre 0 e 100 é:",salFmaiorC,"|")
print("====================================================")
        
        
        
        
        
        