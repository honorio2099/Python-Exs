def somaimposto(taxaimposto,custo):
    custo += custo * (taxaimposto/100) 
    return custo
a=int(input('Qual a Taxa do imposto?'))
b=int(input("Qual o custo?")) 
c = somaimposto(a,b)
print("Novo Valor:",c)