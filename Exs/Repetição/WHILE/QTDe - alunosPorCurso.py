cont = 0
engen = 0
comp = 0
admin = 0
engenIdade = 0
compIdade = 0
adminIdade = 0
while cont != 5:
    curso = input("Curso 1 - Engenharia/ 2 - Computação/ 3 - Administração")
    idade = int(input("Digite a sua idade:"))
    if curso == "1":
        engen += 1
        if idade > 20 and idade < 25:
             engenIdade += 1
             somaIdEng += idade
    elif curso == "2":
        comp += 1
        if idade > 20 and idade < 25:
             compIdade += 1
             somaIdcomp += idade
     elif curso == "3":
        admin += 1
        if idade > 20 and idade < 25:
             adminIdade += 1
             somaIdAdmin += idade
mediIdEng = somaIdEng/engen
mediIdComp = somaIdcomp/comp
mediIdadmin = somaIdAdmin/admin
if mediIdEng < mediIdComp and mediIdEng < mediIdadmin:
    print("A menor Média de idade de alunos é a de Engenharia!")
elif mediIdComp < mediIdadmin:
    print("A menor Média de idade de alunos é a de Computação!")
else:
    print("A menor Média de idade de alunos é a de Administração!")
print("-------------------------------------------------------------")
print("Quantidade de Alunos por curso -")
print("A quantidade de alunos de Engenharia é:",engen)
print("A quantidade de alunos de Computação é:",comp)
print("A quantidade de alunos de Administração é:",admin)
print("-------------------------------------------------------------")
print("Idade de alunos entre 20 e 25 por curso -")
print("A quantidade de alunos entre 20 e 25 anos de Engenharia é:",engenIdade)
print("A quantidade de alunos entre 20 e 25 anos de Computação é:",compIdade)
print("A quantidade de alunos entre 20 e 25 anos de Administração é:",adminIdade)
print("----------------------------------------------------------------------------")



