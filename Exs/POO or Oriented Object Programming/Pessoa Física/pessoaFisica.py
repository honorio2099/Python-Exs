from pessoa import Pessoa

class PessoaFisica(Pessoa):
  __cpf: str
  
  def __init__(self, cpf=None, nome=None, idade=0):
    super().__init__(nome, idade)
    self.__cpf = cpf

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf(self, cpf):
    self.__cpf = cpf
  
  def mostrar(self):
    return super().mostrar() + " e cpf "+self.__cpf

