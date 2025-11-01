#Sa se determine subsecventa de lungime maxima cu proprietatea
def estePrim(p): #Functie ajutatoare pentru a putea afla subsecventa cu o anumita prorprietate
    if p < 2:
        return False
    for i in range(2,p): #cel mai eficient ar sa ma merge pana la (sqrt(n)+1)
        if p % i == 0:
            return False
    return True

#TODO Teste ca sa verificam ca functioneaza optim
#4.Contin doar numere prime
def subsecventa_4(lista):
    pmax, lmax = -1, 0  # subsecventa de lungime maxima p = de unde pornim, l = lungimea
    p, l = -1, 0  # de unde pornim, si lungimea

    for i, e in enumerate(lista):
        if estePrim(e):
            if l == 0: #Incepem o noua secventa
                p = i   #interam peste prima pozitie, si o selectam, in caz contrar marim lungime
            l += 1
            if l > lmax:  # daca gasim o secventa mai lunga
                lmax = l    #lungimea maxima devine lungimea gasita pana acum
                pmax = p    #pozitia din care am inceput
        else:
            l = 0  # resetam lungimea daca urmatorul numar este prim si o luam de la capat

    return pmax, lmax

#5.Au toate elementele in intervalul [0,10]
def elementeInInterval(p):
    if 0 <= p <= 10:
        return True
    return False

#TODO teste pentru a verifica ca functioneaza optim
def subsecventa_8(lista):
    p,l = -1,0
    pmax,lmax = -1,0

    for i,e in enumerate(lista):
        if elementeInInterval(e): #Verifcam daca elementul ales apartine intervalului
            if l == 0: # Initializam un sir nou
                p = i #Si p ia pozitia 0, in caz contrar marim lungimea cu 1
            l += 1
            if l > lmax: #daca lungimea o crecut face o copie pentru
                lmax = l
                pmax = p
        else: # daca nu, incepem din nou, daca nu verifica conditia
            l = 0
    return pmax,lmax

def gcd(a,b):#Daca avem numere negative ar trebui sa le luam modulul ca sa putem lua in scope si pe cele negative
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if b == 0:
        return a
    if a == 0:
        return b
    while b:
        a,b = b,a%b
    return a

def relativPrime(a,b):
    return gcd(a,b) == 1
    #return math.gcd(a,b) == 1

#TODO TESTE CU ASERTIUNI
#3. Oricare doua elemente consecutive sunt relativ prime intre ele (a, b relativ prime daca si numai daca cmmdc(a,b) = 1)
def subsecventa_10(lista):
    p,l = -1,0
    pmax,lmax = -1,0

    if len(lista) < 2:#Nu putem compara daca nu sunt minim doua elemente
        return -1, 0

    for i in range(1,len(lista)):
        if relativPrime(lista[i-1],lista[i]):
            if l == 0:
                p = i - 1 #deoarece lista noastra porneste de la indexul 1, trebuie sa luam start-u; de la 0
                l = 2 #pentru ca avem nevoie de prima pereche
            else:
                l += 1
            if l > lmax:
                lmax = l
                pmax = p
        else:
            l = 0
    return pmax,lmax

#7. oricare doua elemente consecutive difera printr-un numar prim
def diferaprinnumarprim(p,q):
    prim = abs(p-q)
    return estePrim(prim)

#1.   x[i] < x[i+1] < ... < x[i+p]
def subsecventa_1(lista):
    p,l = -1,0
    pmax,lmax = -1,0
    for i in range(1,len(lista)):
        if lista[i-1] < lista[i]:
            if l == 0:
                p = i - 1
                l = 2
            else:
                l += 1
            if l > lmax:
                lmax = l
                pmax = p
        else:
            l = 0
    return pmax,lmax

#7. oricare doua elemente consecutive difera printr-un numar prim
def subsecventa_7(lista):
    p,l = -1,0
    pmax,lmax = -1,0
    for i in range(len(lista)):
        if diferaprinnumarprim(lista[i-1],lista[i]):
            if l == 0:
                p = i - 1
                l = 2
            else:
                l += 1
            if l > lmax:
                lmax = l
                pmax = p
        else:
            l = 0
    return pmax,lmax

'''
def clasadetest():
    assert(diferaprinnumarprim(5,3) == True)
    assert(diferaprinnumarprim(3,5) == True)
    assert(diferaprinnumarprim(1,1) == False)
    assert(diferaprinnumarprim(1,2) == False)
    assert(diferaprinnumarprim(10,20) == False)
    assert(diferaprinnumarprim(10, 21) == True)
    assert(diferaprinnumarprim(-11, -24) == True)
    assert(diferaprinnumarprim(-11, 20) == True)
'''

#2.Contine cel mult trei valori distincte
'''
def celmult3valoridistincte(lista):
    p,l = -1,0
    pmax,lmax = -1,0
    for i in range(0,len(lista)):
        if lista.count(lista[i]) != 3: #folosim count pentru a tine minte de cate ori a parut un element
            if l == 0:
                p = i
                l = 3
            else:
                l += 1

            if l > lmax:
                lmax = l
                pmax = p
        else:
            l = 0
    return pmax,lmax
'''
#5.Au toate elementele egale
def subsecventa_5(lista):
    p,l = -1, 0
    pmax,lmax = -1, 0
    for i in range(len(lista)):
        if lista[i-1] == lista[i]: #conditia necesara ca sa erificam ca eleemtele sunt egale
            if l == 0:
                p = i - 1
                l = 2
            else:
                l += 1
            if l > lmax:
                lmax = l
                pmax = p
        else:
            l = 0
    return pmax,lmax

def main():
    lista = [3,3,3,5,6,4,2,4,7,1,2,1,2,7,1,7,7,7,7,7,7,7]
    p , l = subsecventa_4(lista) #Expected (15,7)
    print(lista[p:p + l]) #Expected [7,7,7,7,7,7,7]

    listaT2 = [1,2,3,4,5,6,7,8,9,10]
    r, m = subsecventa_4(listaT2) #Excepted (1,2)
    print(listaT2[r:r + m]) #Expected [2,3]

    listaT3 = [1,1,1,1,1,1,1,1,1,1,1]
    t,n = subsecventa_4(listaT3) #Expected (-1,0)
    print(listaT3[t:t+n]) #Expected []

    q,w = subsecventa_8(lista)
    print(lista[q:q+w]) #Expected (0,len(lista)) si [3,3,3,5,6,4,2,4,7,1,2,1,2,7,1,7,7,7,7,7,7,7]

    listaT4 = [1,2,3,4,5,-1,6,7,8,0,12,9,10]
    e,r = subsecventa_8(listaT4)
    print(listaT4[e:e+r]) #Expected (0,5) si [1,2,3,4,5]

    listaT5 = [-1, -1, -1, -1, -1, -1, 100, 100, 100, 100, 100, 100]
    s,t = subsecventa_8(listaT5)
    print(listaT5[s:s+t]) #Expected (-1,0) si []

    listaT6 = []
    m,p = subsecventa_8(listaT6)
    print(listaT6[m:m+p])#Expected (-1,0) si []

    listaT7 = [1,2,3,4,5,6,7,8,9,10]
    k,l = subsecventa_10(listaT7)
    print(listaT7[k:k+l]) #Expected (0,len(lista)) si lista

    listaT8 = [1,2,3,4,6,8,16,31,1]
    o,z = subsecventa_10(listaT8)
    print(listaT8[o:o+z]) #Expected (0,4) si [1,2,3,4]

    listaT9 = [0,0,0,0,0,0,1,2,3,3,2,1,-2,-3,-7,-5,-11]
    p,q = subsecventa_10(listaT9)
    print(listaT9[p:p+q]) #Expected [3, 2, 1, -2, -3, -7, -5, -11]

    listaT10 = [1,2,3,4,5,6,7,8,9,10]
    r,s = subsecventa_7(listaT10)
    print(listaT10[r:r+s])#Expected []

    listaT11 = [-11,-8,-1,2,5,1,2,3,4,5,3]
    x,y = subsecventa_7(listaT11)
    print(listaT11[x:x+y])#Expected [-11,-8,-1,2,5]

    listaT12 = [1,2,3,4,5,6,7,8,9,10]
    t,u = subsecventa_5(listaT12)
    print(listaT12[t:t+u])


main()