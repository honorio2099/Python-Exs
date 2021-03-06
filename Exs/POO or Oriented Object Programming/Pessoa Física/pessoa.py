class Pessoa:
  __nome: str
  __idade: int
  
  def __init__(self, nome=None, idade=0):
    self.__nome = nome
    self.__idade = idade

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self,nome):
    self.__nome = nome

  @property
  def idade(self):
    return self.__idade

  @idade.setter
  def idade(self, idade):
    self.__idade = idade

  def mostrar(self):
    return "O cliente "+self.__nome+" tem "+str(self.__idade)+" anos"
 