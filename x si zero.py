#2 jucatori
#ai doar x si 0
#ai o tabla de joc
#ai o tabla de joc 3*3
#ai un castigator daca ai 3 pe linie
tabla=[' ',' ',' ',
       ' ',' ',' ',
    ' ',' ',' ']
remiza=False
scorx=0
scor0=0
while scorx!=3 and scor0!=3:
    tabla = [' ', ' ', ' ',
             ' ', ' ', ' ',
             ' ', ' ', ' ']
    i=0
    k=False
    while k!=True:
        juc1 = int(input("Unde pui?"))
        if tabla[juc1-1]==' ':
            if i%2==0:
                tabla[juc1-1]='x'
            else:
                tabla[juc1-1]='o'
            print(tabla[0:3])
            print(tabla[3:6])
            print(tabla[6:9])
            i+=1
        if tabla[0]==tabla[1]==tabla[2]!=' ':
            k=True
            if i%2==1:
                scorx+=1
                print('Castigatorul este x ')
            else:
                scor0+=1
                print('Castigatorul este o')
        if tabla[3]==tabla[4]==tabla[5]!=' ':
            k=True
            if i%2==1:
                scorx+=1
                print('Castigatorul este x ')
            else:
                scor0+=1
                print('Castigatorul este o')
        if tabla[6]==tabla[7]==tabla[8]!=' ':
            k=True
            if i%2==1:
                scorx+=1
                print('Castigatorul este x ')
            else:
                scor0+=1
                print('Castigatorul este o')
        if tabla[0]==tabla[3]==tabla[6]!=' ':
            k=True
            if i%2==1:
                scorx+=1
                print('Castigatorul este x ')
            else:
                scor0+=1
                print('Castigatorul este o')
        if tabla[1]==tabla[4]==tabla[7]!=' ':
            k=True
            if i%2==1:
                scorx+=1
                print('Castigatorul este x ')
            else:
                scor0+=1
                print('Castigatorul este o')
        if tabla[2]==tabla[5]==tabla[8]!=' ':
            k=True
            if i%2==1:
                scorx+=1
                print('Castigatorul este x ')
            else:
                scor0+=1
                print('Castigatorul este o')
        if tabla[0]==tabla[4]==tabla[8]!=' ':
            k=True
            if i%2==1:
                scorx+=1
                print('Castigatorul este x ')
            else:
                scor0+=1
                print('Castigatorul este o')
        if tabla[2]==tabla[4]==tabla[6]!=' ':
            k=True
            if i%2==1:
                scorx+=1
                print('Castigatorul este x ')
            else:
                scor0+=1
                print('Castigatorul este o')
        if ' ' not in tabla and k==False:
            print('Remiza')
            k=True
            remiza=True
    print('juc1 are', scorx)
    print('juc2 are', scor0)
    if remiza==False:
        temp=scorx
        scorx=scor0
        scor0=temp
    else:
        remiza=True
if scorx==3 :
    print('Castigatorul este x')
elif scor0==3:
    print('Castigatorul este o')




