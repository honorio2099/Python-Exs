class Comodo:
  def __init__(self,largura,comprimento):
    self.largura = largura
    self.comprimento = comprimento
    self.__altura = 2.9

  @property
  def largura(self):
    return self.__largura
    
  @largura.setter
  def largura(self,largura):
    try:
      self.__largura = largura
    except Exception:
      print('Erro!!! - Valor Inválido')
      exit()

@property
def comprimento(self):
  return self.__comprimento
    
  @comprimento.setter
  def comprimento(self,comprimento):
    try:
      self.__comprimento = comprimento
    except Exception:
      print('Erro!!! - Valor Inválido')
      exit()

  @property
  def altura(self):
    return self.__altura
  