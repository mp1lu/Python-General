print('Salut,aici pizzeria Twenty doriti sa comandati ceva?')
x=input('Da sau Nu\n')
total=0
if x=='Da'or x=="da":
    y = input('Pizza sau Suc \n')
    if y=='Pizza'or y=='pizza':
        print('Ce pizza doresti?')
        c = input('Avem aceste feluri de pizza: Capriciosa,Prosciutto \n')
        Capriciosa=27
        Prosciutto=23
        if c=='Capriciosa' or c=='capriciosa':
            total+=Capriciosa
            print('Mai doriti ceva?')
        elif c=='Prosciutto' or c=='prosciutto':
            total+=Prosciutto
            print('Mai doriti ceva?')
        if x=='Da'or x=="da":
            print('Mai doriti inca o pizza sau doriti suc?')

        d = input('Avem aceste feluri de suc:Fanta,Pepsi')
        Fanta=7
        Pepsi=9
        if d=='Fanta' or d=='fanta':
            total+=Fanta
            print('Mai doriti ceva?')
        elif d=='Pepsi' or d=='pepsi':
            total+=Pepsi
            print('Mai doriti ceva?')
elif x=='Nu'or x=='nu':
    print('Ok atunci, la revedere!')
else:
    print('Calmeaza-te te rog!')
print('Totalul dvs este de',total)












