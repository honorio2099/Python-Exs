from exemploClasse import ExemploClasse
from exemploClasseHeranca import ExemploClasseHeranca

x = ExemploClasse()
x.nome = input("digite seu nome: ")
x.idade = int(input("Digite sua idade:"))
x.salario = float(input("Digite sua salario:"))

xh = ExemploClasseHeranca()
xh.nome = input("digite seu nome: ")
xh.idade = int(input("Digite sua idade:"))
xh.salario = float(input("Digite sua salario:"))
xh.bonusMensal = float(input("Digite o bonus:"))

print(x.mostrar())
print(xh.mostrar())
x.calcularNovoSalario(10)
xh.calcularNovoSalario(10)## arrumar
print(x.mostrar())
print(xh.mostrar())

