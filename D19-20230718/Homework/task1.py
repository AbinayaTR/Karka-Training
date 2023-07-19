items_list=[{"name":"Apple","category":"Fruits"},
            {"name":"Carrot","category":"Vegetables"},
            {"name":"Banana","category":"Fruits"},
            {"name":"Broccoli","category":"Vegetables"}]
fruits=[]
vegetables=[]
foods={}
for item in items_list:
    if item['category']=="Fruits":
        fruits.append(item['name'])
    if item['category']=="Vegetables":
        vegetables.append(item['name'])
# foods={"Fruits":fruits,"Vegetables":vegetables}
foods['Fruits']=fruits
foods['Vegetables']=vegetables
print(foods)