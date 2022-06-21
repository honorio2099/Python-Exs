def pali():
    global txt1
    global txt2
    txt1 = input('Digite uma palavra -')
    txt2 = input('Digite outra palavra -')
def inverter(a,b):
    qtdCar1 = len(a)       
    qtdCar2 = len(b)       
    numInv1 = "" 
    numInv2 = ""             
    i1 = (qtdCar1 - 1)   
    i2 = (qtdCar2 - 1)   
    while i1 >= 0:
        numInv1 = numInv1 + a[i1]
        i1 = i1 - 1
    print(a,"invertendo é", numInv1)
    while i2 >= 0:
        numInv2 = numInv2 + b[i2]
        i2 = i2 - 1
    print(b,"invertendo é", numInv2)
    print("------------------------")
    if (len(txt1)) == (len(txt2)) and ((numInv1) == (txt2)) or ((numInv2) == (txt1)):
        print('As duas palavras são Palíndromas uma da outra.')
    else:
        print('Elas não são Palíndromas.')
pali()
inverter(txt1,txt2)
