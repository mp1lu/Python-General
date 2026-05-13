piatra = '''
    __
---'   )
      ()
      ()
      ()
---.()
'''
hartie = '''
    __
---'   )
          __)
          __)
         __)
---.__)
'''
foarfece = '''
    __
---'   )
          __)
       __)
      (__)
---.(___)'''

print(piatra)
print(hartie)
print(foarfece)
puncte1=0
puncte2=0
while puncte1!=3 and puncte2!=3:
    jucator1 = input('Alege  ''Piatra'' ,''Foarfeca'' ,''Hartie\n')
    jucator2 = input('Alege  ''Piatra'',''Foarfeca'' ,''Hartie\n')
    if jucator1=='Piatra' and jucator2=='Foarfeca':
        print('Jucator1 castiga')
        puncte1+=1
    if jucator1 == 'Piatra' and jucator2 == 'Hartie':
        print('Jucator2 castiga')
        puncte2+=1
    if jucator1 == 'Foarfeca' and jucator2 == 'Hartie':
        print('Jucator1 castiga')
        puncte1+=1
    if jucator1 == 'Foarfeca' and jucator2 == 'Piatra':
        print('Jucator2 castiga')
        puncte2+=1
    if jucator1 == 'Hartie' and jucator2 == 'Piatra':
        print('Jucator1 castiga')
        puncte1+=1
    if jucator1 == 'Hartie' and jucator2 == 'Foarfeca':
        print('Jucator2 castiga')
        puncte2+=1
    elif jucator1 == jucator2 :
        print('Remiza')
if puncte1>puncte2:
    print('Jucator1 esti castigatorul', 'Best of 3')
elif puncte1<puncte2:
    print('Jucator2 esti castigatorul', 'Best of 3')







