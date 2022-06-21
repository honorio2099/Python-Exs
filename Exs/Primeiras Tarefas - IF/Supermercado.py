print("=====================================================================")
print("                      Supermercado Gotas Azuis                       ")
print("---------------------------------------------------------------------")
print("                      | Gasto Médio | Crédito |                      ")
print("                      |  0 a 100    | 0 %     |                      ")
print("                      | 101 a 500   | 15 %    |                      ")
print("                      | 501 a 800   | 25 %    |                      ")
print("                      |acima de 801 | 35 %    |                      ")
print("---------------------------------------------------------------------")
print("Informações Pessoais -")
nome = input("Cliente, Informe seu nome: ")
gasto = float(input("Por favor, Informar o Gasto Médio do Último ano: R$"))
print("---------------------------------------------------------------------")
if (gasto >= 0) and (gasto <= 100):
     credito = gasto 
     percentual = "0 %"
elif (gasto >= 101) and (gasto <= 500):
     credito = (gasto * 1.15)
     percentual = "15 %"
elif (gasto >= 501) and (gasto <= 800):
     credito = (gasto * 1.25)
     percentual = "25 %"
elif (gasto >= 801):
     credito = (gasto * 1.35)
     percentual = "35 %"
print("O",nome,"têm direito a",percentual,"de Crédito Pessoal.")
print("O Crédito Pessoal do cliente",nome,"é de R$",credito)
print("=====================================================================")