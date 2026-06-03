    # jocul de spanzuratoarea:
    # se alege un cuvant random de mai jos
    # se afiseaza pe ecran simbolic faptul ca avem un cuvant cu aceasi lungime
    # la fiecare litera corecta se afiseaza cuvantul cu acele litere in loc de "_"
    # la 6 greseli pierzi
    # langa cuvantul bun se afiseaza si literele gresite sa nu se faca repetitii
import random


words = ["casa", "apa", "paine", "soare", "luna",
    "caine", "pisica", "carte", "masina", "copac",
    "floare", "munte", "rau", "mare", "cer",
    "noapte", "zi", "foc", "vant", "ploaie",
    "zapada", "gheata", "piatra", "lemn", "frunza",
    "radacina", "pamant", "nisip", "val", "stanca",
    "pasare", "peste", "cal", "vaca", "oaie",
    "porc", "gaina", "rata", "iepure", "vulpe",
    "lup", "urs", "cerb", "acvila", "fluture",
    "albina", "furnica", "sarpe", "broasca", "melc",
    "masa", "scaun", "pat", "usa", "fereastra",
    "perete", "podea", "tavan", "scara", "curte",
    "gradina", "drum", "pod", "turn", "biserica",
    "scoala", "spital", "magazin", "piata", "parc",
    "tata", "mama", "frate", "sora", "bunic",
    "bunica", "prieten", "copil", "baiat", "fata",
    "om", "femeie", "barbat", "mana", "picior",
    "cap", "ochi", "nas", "gura", "ureche",
    "inima", "suflet", "minte", "vis", "iubire",
    "bucurie", "tristete", "frica", "speranta", "liniste"
]
x=random.choice(words)
greseli=0
cuvant='_'* len(x)
print(cuvant)
cuvant=list(cuvant)
list=[]
while '_' in cuvant and greseli<6:
    v=input('Ce litera vrei?').lower()
    if v[0] in x:
        i=0
        while i<len(x):
            if v[0]==x[i]:
                cuvant[i]=v[0]
            i=i+1

    elif v[0] not in x:
        greseli=greseli+1
        print('Ai',greseli, 'greseli')
    temp=""
    for l in cuvant:
        temp=temp+l
    print(temp)
    list.append(v[0])
    print(list)

if greseli==6:
    print('Ai pierdut')
    print('Cuvantul a fost',x)
else:
    print('Ai castigat')








