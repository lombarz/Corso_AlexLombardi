""" Scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no """

def is_palindroma(stringa):
    lista=[]
    pal='True'
    for elemento in stringa:
        if elemento.isalpha():#elimina vari spazi e/o punteggiatura/ numeri
          lista.append(elemento)
    lung=len(lista)
    for num in range(lung//2):
       if lista[num]!=lista[-num-1]:#controllo palindromo
          pal='False'
          break#al primo errore stoppa il ciclo, risparmio potenza di calcolo
    return pal
    

frase=input("Inserisci frase: ")
if is_palindroma(frase)=='True':
   print(frase," è palindroma")
else:
   print(frase," non è palindroma")