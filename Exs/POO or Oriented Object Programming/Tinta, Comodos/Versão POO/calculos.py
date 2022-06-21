class Calculos:

  def calcularAreaFF(self,comodo):
    self.__frentefundo = (comodo.largura * comodo.altura) * 2
    return self.__frentefundo

  def calcularAreaParedes(self,comodo):
    sef.__paredes = (comodo.altura * comodo.comprimento) * 2
    return sef.__paredes
  def calcularAreaTeto(self,comodo):
    self.__teto = comodo.largura * comodo.comprimento
    return self.__teto
  def AreaTotal(self,comodo):
    self.__areatotalComodo = self.__calcularAreaFF(comodo) +   self.__calcularAreaParedes(comodo) +   self.__calcularAreaTeto(comodo)
    return areatotalComodo
  def calcularLitrosTinta(self):
    if self.__areaTotal(comodo) <= 0:
      print('Valor = Zero - NÃO É POSSÍVEL CALCULAR')
    litrostinta = self.areaTotal(comodo)/10
    return litrostinta
