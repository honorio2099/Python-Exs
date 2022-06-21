from exemploClasse import ExemploClasse

class ExemploClasseHeranca(ExemploClasse):
# criando classe GERENTE
  __bonusMensal: float

#  def __init__(self, bonusMensal):
#    self.__bonusMensal = bonusMensal

  @property
  def bonusMensal(self):
    return self.__bonusMensal

  @bonusMensal.setter
  def bonusMensal(self, bonusMensal):
    self.__bonusMensal = bonusMensal
  
  def mostrar(self):
    return ExemploClasse.mostrar(self) + " mais o bonus Mensal de R$ " + str(self.__bonusMensal)
  
  