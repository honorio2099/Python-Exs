print('***********************************')
print('    CALCULADORA DE TINTAS          ')
print('***********************************')
print('Digite a largura do comodo:')
largura = float(input())
print('Digite o comprimento do comodo:')
comprimento = float(input())
altura = 2.9
frentefundo = (largura * altura) * 2
paredes = (altura * comprimento) * 2
teto = largura * comprimento
areatotalComodo = frentefundo + paredes + teto
litrostinta = areatotalComodo/10
print('A área total é igual a =>',areatotalComodo)
print('Litross de tinta são =>',litrostinta)