#2 jucatori
#ai doar x si 0
#ai o tabla de joc
#ai o tabla de joc 3*3
#ai un castigator daca ai 3 pe linie
tabla=[' ',' ',' ',
       ' ',' ',' ',
       ' ',' ',' ']
i=0
k=False
while i<9:
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
            print('Castigatorul este x ')
        else:
            print('Castigatorul este o')
    if tabla[3]==tabla[4]==tabla[5]!=' ':
        k=True
        if i%2==1:
            print('Castigatorul este x ')
        else:
            print('Castigatorul este o')
    if tabla[6]==tabla[7]==tabla[8]!=' ':
        k=True
        if i%2==1:
            print('Castigatorul este x ')
        else:
            print('Castigatorul este o')
    if tabla[0]==tabla[3]==tabla[6]!=' ':
        k=True
        if i%2==1:
            print('Castigatorul este x ')
        else:
            print('Castigatorul este o')
    if tabla[1]==tabla[4]==tabla[7]!=' ':
        k=True
        if i%2==1:
            print('Castigatorul este x ')
        else:
            print('Castigatorul este o')
    if tabla[2]==tabla[5]==tabla[8]!=' ':
        k=True
        if i%2==1:
            print('Castigatorul este x ')
        else:
            print('Castigatorul este o')
    if tabla[0]==tabla[4]==tabla[8]!=' ':
        k=True
        if i%2==1:
            print('Castigatorul este x ')
        else:
            print('Castigatorul este o')
    if tabla[2]==tabla[4]==tabla[6]!=' ':
        k=True
        if i%2==1:
            print('Castigatorul este x ')
        else:
            print('Castigatorul este o')





