import os
def interface():
    print("===========================")
    print("|         TABUADA         |")
    print("===========================")
def tabuada():
    result = 1
    n = int(input('Digite a Tabuada escolhida:'))
    while result < 11:
        print(result,'X',n,'=',result * n)
        result += 1
option = 0
c = 0
while c != 10:
    os.system('clear')
    interface()
    tabuada()
    option = int(input("Deseja Escolher Outra Tabuada? [1 - Sim] ou [2 - Não]"))
    if option == 1:
        c += 1
    elif option == 2:
        break
    
    
    
    
    
    
    
    