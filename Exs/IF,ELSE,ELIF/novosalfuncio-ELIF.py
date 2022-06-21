sal = float(input("Digite o salário do funcionário:"))
if sal < 500:
    novosal = sal * 1.15
elif sal >= 500 and sal <= 100:
    novosal = sal * 1.05
elif sal > 1000:                # elif é um else e if juntos, é um else para o if anterior e um novo if
    novosal = sal * 1.10        # sem ter que ficar criando uma escada de identação 
print("O novo salário é R$",novosal)