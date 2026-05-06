print('Salut,aici pizzeria Twenty doriti sa comandati ceva?')
x=input('Da sau Nu\n')
total=0
while x=='Da' or x=='da':
    y = input('Pizza sau Suc \n')
    if y=='Pizza'or y=='pizza':
        print('Ce pizza doresti?')
        c = input('Avem aceste feluri de pizza: Capriciosa,Prosciutto,Hawai,Diavola,Tonno \n')
        Capriciosa=27
        Prosciutto=23
        Hawai=30
        Diavola=24
        Tonno=23
        if c=='Capriciosa' or c=='capriciosa':
            total+=Capriciosa
        elif c=='Prosciutto' or c=='prosciutto':
            total+=Prosciutto
        elif c=='Hawai' or c=='hawai':
                total += Hawai
        elif c=='Diavola' or c=='diavola':
            total += Diavola
        elif c=='Tonno' or c=='tonno':
            total += Tonno
    if y=='Suc' or y=='suc':
        d = input('Avem aceste feluri de suc:Fanta,Pepsi,Lipton,limonada,Cola')
        Fanta=7
        Pepsi=9
        Lipton=6
        Limonada=10
        Cola=8
        if d=='Fanta' or d=='fanta':
            total+=Fanta
        elif d=='Pepsi' or d=='pepsi':
            total+=Pepsi
        elif d=='Lipton' or d=='lipton':
            total+=Lipton
        elif d=='Limonada' or d=='limonada':
            total+=Limonada
        elif d=='Cola' or d=='cola':
           total+=Cola
    print('Mai doriti ceva?')
    x=input('Da sau Nu\n')
else:
 if x=='Nu'or x=='nu':
    print('Ok atunci, la revedere!')
 else:
    print('Calmeaza-te te rog!',total)
print('Totalul dvs este de',total)












