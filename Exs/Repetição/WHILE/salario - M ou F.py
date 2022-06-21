cont = 0
somaF = 0
somaM = 0
while cont != 5:
    option = input("Qual o seu gênero? Escolha - 1 [Masculino] ou 2 - [Feminino]")
    if option == 1:
        salM = float(input("Digite o seu salário:"))
        somaM += salM
        masculino += 1
    if option == 2:
        salF = float(input("Digite o seu salário:"))
        somaF += salF
        feminino += 1
    cont += 1
mediaM = salM/masculino
mediaF = salF/feminino
print("Salário masculino:",mediaM)
print("Salário feminino:",mediaF)
print("Soma do salário masculino:",somaM)
print("Soma do salário feminino:",somaF)
