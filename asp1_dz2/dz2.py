# Definisanje struktura cvor
class Cvor:
    """
    Struktura podataka Cvor:
        predstavlja jedan cvor - jedno stanje sudoku-a
        Metodi:
            .matrix - pravi kopija matrici da ne bi se izgubile podaci iz originala
            .sinovi - lista svih (validnih) sinova tog cvora
    """
    def __init__(self, matrix):
        self.matrix = [[elem for elem in vrsta] for vrsta in matrix]
        self.sinovi = []

def provera_stanja(matrix):
    """ :parameter matrix: matrica (lista liste) koja predstavlja neko stanje u sudoku
    Proverava stanje matrice redom:
        prvo da li su ispravne vrste, pa kolone, pa podmatrice
    Na kraju proverava da li je matrica barem 30% popunjena
    :return _Boolean: True ili False u zavisnosti od validnosti trenutno proveravanog stanja
    """
    # proverka vrste:
    for i in range(len(matrix)):
        lista_elementa = [0, 0, 0, 0]
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                if lista_elementa[matrix[i][j]-1]==1:
                    return False
                else:
                    lista_elementa[matrix[i][j]-1]=1

    #proverka kolona:
    for i in range(len(matrix)):
        lista_elementa = [0, 0, 0, 0]
        for j in range(len(matrix[i])):
            if matrix[j][i] != 0:
                if lista_elementa[matrix[j][i]-1]==1:
                    return False
                else:
                    lista_elementa[matrix[j][i]-1]=1

    #proverka podmatrice:
    for i in range(0, 4, 2):
        for j in range(0, 4, 2):
            lista_elementa = [0, 0, 0, 0]
            for x in range(i, i+2):
                for y in range(j, j+2):
                    if matrix[x][y] != 0:
                        if lista_elementa[matrix[x][y]-1]==1:
                            return False
                        else:
                            lista_elementa[matrix[x][y]-1]=1

    #proverka popunjenosti matrice
    brojac_elemenata = 0
    for vrsta in matrix:
        for elem in vrsta:
            if elem != 0:
                brojac_elemenata+=1
    if brojac_elemenata<5:
        return False

    return True

def stablo_odlucivanja(pocetno_stanje):
    """
    :parameter pocetno_stanje: matrica uneta preko standardnog ulaza
    :return koren: vraca koreni cvor stabla omogucavajuci manipulaciju sa celom stablom
    Formira stablo odlucivanja
    """
    red = [] #struktura red kreirana ciljem formiranje svi cvorovi redom
    koren = Cvor(pocetno_stanje)
    red.append(koren)

    while(red):
        obr_cvor = red.pop(0)
        matrica = [[elem for elem in vrsta] for vrsta in obr_cvor.matrix]

        for i in range(len(matrica)):
            for j in range(len(matrica[i])):
                if matrica[i][j] == 0:
                    for sudoku_broj in range (1, 5):
                        matrica[i][j] = sudoku_broj
                        if provera_stanja(matrica):
                            val_cvor = Cvor(matrica)
                            obr_cvor.sinovi.append(val_cvor)
                            red.append(val_cvor)
                            #red je implementiran kao listu koja ubacuje elemenata na kraju, a ih izbacuje sa pocetka
                        matrica[i][j] = 0
    return koren

def preorder_obilazak_stabla(koren):
    stack = []
    stack.append(koren)
    while(len(stack)!=0):
        next = stack.pop()
        while(next!=None):
            if(len(next.sinovi)>=2):
                for i in range(1, len(next.sinovi)):
                    stack.append(next.sinovi[i])
            for i in range(len(next.matrix)):
                for j in range(len(next.matrix[i])):
                    print(next.matrix[i][j], end="")
                    if j != len(next.matrix[i])-1:
                        print(" | ", end="")
                print("\n--------------")
            print("\n\n")
            if(len(next.sinovi)>=1):
                next = next.sinovi[0]
            else:
                next = None

def ispis_resenja(koren):
    tr_matrica = koren.matrix
    mat_resenje = tr_matrica
    resenje = True

    while resenje:
        resenje = False
        for i in range(len(mat_resenje)):
            for j in range(len(mat_resenje[i])):
                if mat_resenje[i][j] == 0:
                    for broj in range(1, 5):
                        tr_matrica[i][j] = broj
                        if provera_stanja(tr_matrica):
                            mat_resenje = tr_matrica
                            print(tr_matrica)
                            resenje = True
                            break
                    if resenje:
                        break
        for i in range(len(mat_resenje)):
            for j in range(len(mat_resenje[i])):
                if mat_resenje[i][j] == 0:
                    resenje = True

### main ###

matrix = [[int(elem) for elem in input().split()] for i in range(4)]

#matrix = [[3,0,4,0],[0,1,0,2],[0,4,0,3],[2,0,1,0]]
koren = stablo_odlucivanja(matrix)
preorder_obilazak_stabla(koren)
ispis_resenja(koren)


    