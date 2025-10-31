#Sa se determine subsecventa de lungime maxima cu proprietatea
#4.Contin doar numere prime

def estePrim(p): #Functie ajutatoare pentru a putea afla subsecventa cu o anumita prorprietate
    if p < 2:
        return False
    for i in range(2,p): #cel mai eficient ar sa ma merge pana la (sqrt(n)+1)
        if p % i == 0:
            return False
    return True

#TODO Teste ca sa verificam ca functioneaza optim
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
            l = 0  # resetam lungimea

    return pmax, lmax


def main():
    lista = [3,3,3,5,6,4,2,4,7,1,2,1,2,7,1,7,7,7,7,7,7,7]
    p , l = subsecventa_4(lista) #Expected (15,7)
    print(lista[p:p + l]) #Expected [7,7,7,7,7,7,7]

    listaT2 = [1,2,3,4,5,6,7,8,9,10]
    r, m = subsecventa_4(listaT2) #Excepted (1,2)
    print(listaT2[r:r + m]) #Expected [2,3]

main()