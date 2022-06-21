salame = float(input("Digite o valor do Salame:"))
Bisteca = float(input("Digite o valor da Bisteca:"))
CoxaFrango = float(input("Digite o valor da Coxa de Frango:"))
Total = salame + Bisteca + CoxaFrango
print("O total a pagar é:",Total)
pgmt = float(input("Digite O valor a Pagar -"))
while (pgmt <= Total):
     print("Favor, Pagar o que Deve")
     if pgmt >= Total:
         break 
     pgmt = float(input("Digite O valor a Pagar -"))
Troco = Total - pgmt
import os
os.system('clear') or None

print("---------------------------------------------------------")
print("         CARREFOUR COMERCIO E INDUSTRIA LTDA             ")
print("|01/04/2022 15:48:50            CCF: 186715 COO: 385184  ")
print("---------------------------------------------------------")
print("                     CUPOM FISCAL                        ")
print("ITEM CÓDIGO DESCRIÇÃO QTD.UN.VL UNIT R$ ST A/T VL ITEM R$")
print("---------------------------------------------------------")
print("001   00783462   Bisteca                  1|(R$", Bisteca ,")")
print("002   00783462   Salame                   2|(R$", salame ,")")
print("003   00783462   Coxa de Frango           3|(R$", CoxaFrango ,")")
print("---------------------------------------------------------")
print("TOTAL              R$                      R$", Total ,")")
print("Dinheiro                                      ", pgmt ,")")
print("Troco R$                                      ", Troco ,")")
print("---------------------------------------------------------")
print("ITEM(S) COMPRADOS: (3)")
print("DRT: 901275396    PDV: 9          CUPOM: 37329")
print("PROCON - FONE: 3212 - 1500")
print("---------------------------------------------------------")
Time = input("Aperte Enter para prosseguir;")
import os
os.system('clear') or None
salameInfla = float(input("Digite o valor do Salame:"))
bistecaInfla = float(input("Digite o valor da Bisteca:"))
coxafrangoInfla = float(input("Digite o valor da Coxa de Frango:"))
Total = salame + Bisteca + CoxaFrango
print("O total a pagar é:",Total)
pgmt = float(input("Digite o valor a Pagar -"))
if (pgmt <= Total): 
   print("Favor, Pagar o que Deve")
Troco = Total - pgmt
import os
os.system('clear') or None

print("         CARREFOUR COMERCIO E INDUSTRIA LTDA             ")
print("|01/05/2022 17:22:39            CCF: 186715 COO: 385184  ")
print("---------------------------------------------------------")
print("                     CUPOM FISCAL                      ")
print("ITEM CÓDIGO DESCRIÇÃO QTD.UN.VL UNIT R$ ST A/T VL ITEM R$")
print("---------------------------------------------------------")
print("001   00783462   Salame                  1|(R$", salameinfla ,")")
print("002   00783462   Bisteca                 2|(R$", bistecainfla ,")")
print("003   00783462   Coxa de Frango          3|(R$", coxafrangoinfla ,")")
print("---------------------------------------------------------")
print("TOTAL              R$                      R$", Total ,")")
print("Dinheiro                                      ", pmto ,")")
print("Troco R$                                      ", Troco ,")")
print("---------------------------------------------------------")
print("ITEM(S) COMPRADOS: (3)")
print("DRT: 901275396    PDV: 9          CUPOM: 56782")
print("PROCON - FONE: 3212 - 1500")
print("---------------------------------------------------------")
Time = input("Aperte Enter para prosseguir;")
import os
os.system('clear') or None
Infla1 = ((salame/salameInfla)-1)*100
Infla2 = ((Bisteca/bistecainfla)-1)*100
Infla3 = ((CoxaFrango/coxafrangoinfla)-1)*100
print("==========================================")
print("A inflação da Coxa de Frango foi", Infla3)
print("A inflação da Bisteca foi", Infla2)
print("A inflação do Salame foi", Infla1)
