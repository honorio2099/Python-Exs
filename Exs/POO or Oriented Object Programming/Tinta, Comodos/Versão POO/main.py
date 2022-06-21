from calculos import Calculos
from comodo import Comodo
print('***********************************')
print('    CALCULADORA DE TINTAS          ')
print('***********************************')
print('Digite a largura do comodo:')
try:
  largura = float(input())
except Exception:
  print('Não aceita letras, né amigo(a)! Favor colocar números!!!')
  exit()
print('Digite o comprimento do comodo:')
comprimento = float(input())
altura = 2.9

calculos = Calculos()
quarto = Comodo(largura,comprimento)
areatotal = calculos.AreaTotal(quarto)

print()
print('A área total é igual a =>',areatotal)
print('Litros de tinta são =>',calculos.calcularLitrosTinta)