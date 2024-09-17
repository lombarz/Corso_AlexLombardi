import random
import numpy as np

def creazione_matrix():
    righe=int(input("numero righe"))
    colonne= int(input("numero colonne"))
    matrice=np.random.randint(0, 10, (righe, colonne))
    return matrice
def estrazione_sottomatrice(matrice):
    # Dimensioni della sottomatrice centrale
    m=int(input("righe sottomatrice:"))
    n=int(input("colonne sottomatrice:")) 
    righe,colonne=matrice.shape
    start_row = (righe - m) // 2
    start_col = (colonne - n) // 2
    sottomatrice_centrale = matrice[start_row:start_row + m, start_col:start_col + n]
    return sottomatrice_centrale
def trasposta(matrice):
    transposta=matrice.T
    return transposta
def somma_matrix(matrice):
    righe,colonne=matrice.shape
    matrice3=matrice
    matrice3=matrice3.reshape((colonne+righe))  
    somma=np.sum(matrice3)
    return somma
def moltiplica(matrice):
    righe,colonne=matrice.shape
    matricex=np.zeros((righe,colonne))
    moltiplicata=np.zeros((righe,colonne))
    for i in range(righe):
        for j in range(colonne):
          matricex[i][j]=int(input(f"inserisci il valore della casella {i},{j}"))
    for r in range(righe):
        for s in range(colonne):
          moltiplicata[r][s]=matricex[r][s]*matrice[r][s]
    return moltiplicata
def media(matrice):
    righe,colonne=matrice.shape
    somma=somma_matrix(matrice)
    media=somma/(righe+colonne)
    return media
def determinante(matrice):
    righe,colonne=matrice.shape
    if righe==colonne:
        determinante = np.linalg.det(matrice)
        print("Il determinante è",determinante)
    else:
        print("la matrice non è quadrata")
def traccia(matrice):
    righe,colonne=matrice.shape
    traccia=0
    if righe<colonne:
      for k in range(righe):
          traccia+=matrice[k][k]
    else:
        for k in range(colonne):
          traccia+=matrice[k][k]
    return traccia

    



while True:
    scelta=input("cosa vuoi fare? 1 crea matrice 2 estrai sottomatrice 3 trasponi matrice 4 somma elementi 5media 6 moltiplica 7 traccia 8 determinante 9 esci ")
    if scelta=='1':
        matrix=creazione_matrix()
        print("Hai creato la matrice",matrix)
    elif scelta=='2':
        try:
            sottomat=estrazione_sottomatrice(matrix)
            print("La sottomatrice è",sottomat)
        except:
            print("non hai ancora una matrice, prima devi crearla")
    elif scelta=='3':
        try:
            trans=trasposta(matrix)
            print("La matrice transposta è", trans)
        except:
            print("non hai ancora una matrice, prima devi crearla")
    elif scelta=='4':
        try:
            sum=somma_matrix(matrix)
            print("La somma è",sum)
        except:
            print("non hai ancora una matrice, prima devi crearla")
    elif scelta=='9':
        break
    elif scelta=='6':
        try:
            prodotto=moltiplica(matrix)
            print("La moltiplicazione è",prodotto)
        except:
            print("non hai ancora una matrice, prima devi crearla")
    elif scelta=='5':
        try:
            mean=media(matrix)
            print("La media degli elementi è",mean)
        except:
            print("non hai ancora una matrice, prima devi crearla")
    elif scelta=='7':
        try:
            track=traccia(matrix)
            print("La traccia è", track)
        except:
            print("non hai ancora una matrice, prima devi crearla")
    elif scelta=='8':
        try:
            determinante(matrix)
        except:
            print("non hai ancora una matrice, prima devi crearla")
    else:
        print("Scelta non valida")
    