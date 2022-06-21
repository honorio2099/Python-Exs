from pessoa import Pessoa
from pessoaFisica import PessoaFisica

pessoa1 = Pessoa()
pessoaFis1 = PessoaFisica()

pessoa1.nome = "Ana"
pessoa1.idade = 18

pessoaFis1.nome = "José"
pessoaFis1.idade = 19
pessoaFis1.cpf = '123.456.789-00'

print(pessoa1.mostrar())
print(pessoaFis1.mostrar())
