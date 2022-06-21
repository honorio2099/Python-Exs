receitas = {
    'Brigadeiro':['Leite Condesado','Chocolate'],
    'Pudim':['Leite', 'Leite Condensado', 'Ovos'],
    'Manjar':['Leite de Coco', 'Coco Ralado']
}
#print(receitas)
receitas['Gelatina'] = ['Àgua','Gelatina']
#print(receitas.items())
for doce,ingredientes in receitas.items():
    print("Receita:", doce)
    for itemIng in ingredientes:
        print("Ingredientes:",itemIng)

if "Pudim" in receitas:
    del receitas["Pudim"]

print(receitas)


