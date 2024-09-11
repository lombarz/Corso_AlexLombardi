""" Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave """

def de_cifratura(frase, chiave):
  alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  listadec=[]
  for elemento in frase:
    if elemento.isalpha():
      numero=alfabeto.index(elemento)
      listadec.append(alfabeto[(numero+chiave)%26])#utilizzo il modulo di resto per uscire dal problema del range!
    else:
      listadec.append(elemento)
  frasedec="".join(listadec)
  return frasedec

chc=int(input("Vuoi cifrare (1) o decifrare (2) la tua frase? "))
if chc==1:
   know=input("Inserire la frase: ")
   key= int(input("Inserire il valore della chiave: "))
   unknow=de_cifratura(know,key)
   print("La frase cifrata è: ", unknow)
else:
   unknow=input("Inserire la frase: ")
   key= int(input("Inserire il valore della chiave: "))
   know=de_cifratura(unknow,-key)#-key per decifrare
   print("La frase decifrata è: ", know)
          