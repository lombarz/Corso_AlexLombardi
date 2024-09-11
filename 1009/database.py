""" Scrivete un programma che prenda i nomi degli alunni di una
classe e i loro voti, quando l’utente scrive media il programma
andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
media dei voti.
Esempio:
Nome: Giovanni , Media: 7.5
Nome: Alfredo , Media: 9
Nome: Michela, Media 10 """

def new_student():
  nome=input("Nome: ")
  cognome=input("Cognome: ")
  numero_voti=int(input("quanti voti ha lo studente?"))
  lista_voti=[]
  tot_voti=0
  for num in range(numero_voti):
    voto=int(input("Inserisci voto: "))
    lista_voti.append(voto)
    tot_voti+=voto
  media=tot_voti/numero_voti
  dizionario={"Nome: ": nome, "Cognome: ": cognome, "lista voti: ": lista_voti, "Media voti: ": media}
  return dizionario

print("Benvenuto nel database scolastico")
chc='True'
id=0
database={}
while chc=='True':
  chc2=input("Inserire nuovo studente? s n")
  if chc2=='n':
    chc='False'
  else:
    id+=1
    database[id]=new_student()
scelta=input("Vuoi stampare le medie? s n")
if scelta=='s':
  for x in database:
    print(database[x])
