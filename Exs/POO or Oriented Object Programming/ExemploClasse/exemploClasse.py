class ExemploClasse:
  #criando a classe FUNCIONARIO
  __nome: str
  __idade: int
  __salario: float
    
  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome):
    self.__nome = nome  

  @property
  def salario(self):
    return self.__salario

  @salario.setter
  def salario(self, salario):
    self.__salario = salario  
  
  @property
  def idade(self):
    return self.__idade

  @idade.setter
  def idade(self, idade):
    if idade > 0:
      self.__idade = idade  
    else:
      self.__idade = 0

  def calcularNovoSalario(self, porc):
    self.__salario = self.__salario + (self.__salario * porc/100)

  def mostrar(self):
    return self.__nome + " tem " + str(self.__idade) + " anos e R$ " + str(self.__salario) + " de salário mensal"
  

