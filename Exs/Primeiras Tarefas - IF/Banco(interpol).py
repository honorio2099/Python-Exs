print("=====================================================================")
print("                         Banco do Sul                                ")
print("---------------------------------------------------------------------")
print("Formas de pagamento - ")
print("1 - Em 6 meses de juros de 8%                                        ")
print("2 - Em 10 meses de juros de 14%                                      ")
print("3 - Em 15 meses de juros de 20%                                      ")
print("4 - Em 24 meses de juros de 30%                                      ")
print("---------------------------------------------------------------------")
print("Informações Pessoais -")
nome = input("Por favor, Informe seu Nome:")
emprestimo = float(input("Empréstimo Desejado: "))
pgmto = int(input("Qual forma de pagamento deseja realizar? (Escolha uma opção):"))
print("---------------------------------------------------------------------")
if emprestimo <= 10000:
     juros = 1.03
     emprestimo *= juros
elif emprestimo <= 20000:
     juros = 1.05
     emprestimo *= juros
elif emprestimo <= 30000:
     juros = 1.07
     emprestimo *= juros
elif emprestimo > 30000:
     juros = 1.10
     emprestimo *= juros
     
if pgmto == 1:
     juros = (emprestimo * 1.08)
     meses = 6
     parcelas = juros/meses
     emprestimo += juros
elif pgmto == 2:
     juros = (emprestimo * 1.14)
     meses = 10
     parcelas = juros/meses
     emprestimo += juros
elif pgmto == 3:
     juros = (emprestimo * 1.20)
     meses = 15
     parcelas = juros/meses
     emprestimo += juros
elif pgmto == 4:
     juros = (emprestimo * 1.30)
     meses = 24
     parcelas = juros/meses
     emprestimo += juros
     
print(f"Cliente {nome}, o Empréstimo desejado somado com os juros ficará em {round(emprestimo,4)},e as parcelas ficarão em {round(parcelas,4)} de {meses} meses.")
print("================================================================================================================================")