import math
print("=====================================================")
print("                       MENU                          ")
print("-----------------------------------------------------")
print("1 - Área da Circunferência: A = 3,1415 * R²")
print("2 - Perímetro da Circunferência: P = 2 * 3,1415 * R")
print("-----------------------------------------------------")
option = float(input("Escolha a sua Opção: "))
raio = float(input("Digite o Valor do Raio - "))
print("=====================================================")
if option == 1:
  print("A opção escolhida foi Área:",3.1415 * (math.pow(raio,2)))
if option == 2:
  print("A opção escolhida foi Perímetro:",2 * 3.1415 * raio)