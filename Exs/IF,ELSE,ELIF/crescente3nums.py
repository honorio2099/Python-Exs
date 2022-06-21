n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite outro número:'))
print("==========================================")
if (n1>n2) and (n1>n3) and (n2<n3):
     print("Ordem crescente:",n2,"e",n3,"e",n1)
elif (n1>n2) and (n1>n3) and (n3<n2):
     print("Ordem crescente:",n3,"e",n2,"e",n1)
elif (n2>n1) and (n2>n3) and (n1<n3):   
     print("Ordem crescente:",n1,"e",n3,"e",n2)
elif (n2>n1) and (n2>n3) and (n3<n1):
     print("Ordem crescente:",n3,"e",n1,"e",n2)
elif (n3>n1) and (n3>n2) and (n1<n2):
     print("Ordem crescente:",n1,"e",n2,"e",n3)
elif (n3>n1) and (n3>n2) and (n2<n1):
     print("Ordem crescente:",n2,"e",n1,"e",n3)
print("|-----------------------------------------|")
         
         
         
         