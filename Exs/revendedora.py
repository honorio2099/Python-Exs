print("=====================================")
print("       Revendedora Sul Ltda")
print("=====================================")
print()
nome = input('Diga o nome do(a) vendedor(a) escolhido(a)")
quantidade = int(input("Diga a quantidade de carros vendidas pelo(a)",nome))
salfixo = 3.500
vendas = float(input("Seu valor Total de vendas é:"))
comissaovendas = (vendas * 5/100)
comissao = quantidade * 50
finalsal = comissao + salfixo + comissaovendas
print("=====================================")
print("A comissão por carro no mês é",comissao)
print("Comissão das vendas de carros é",comissaovendas)
print("O salário do(a) vendedor(a)",nome,"é",finalsal)