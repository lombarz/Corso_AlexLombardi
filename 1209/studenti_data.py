""" creare un programma per la gestione degli studenti di una scuola, 
all'avvio se il db è presente legge i dati da db altrimenti lo crea, 
l'utente puoi inserire studenti e voti all'interno del db """

def lettura_file(nome_testo):
    with open(nome_testo,"r") as myfile:
        return myfile.read()

class Student():
  def __init__(self,id,nome,cognome,media_italiano,media_scienza,media_inglese):
     self.id=id
     self.nome=nome
     self.cognome=cognome
     self.media_ita=media_italiano
     self.media_sci=media_scienza
     self.media_ing=media_inglese
  def stringa_stud(self):
    stringa_studente="\n"+self.id+","+self.nome +","+self.cognome +","+self.media_ita +","+self.media_sci+","+self.media_ing
    return stringa_studente


scelta='True'
lista_id=[]
while scelta=='True':
  id=input("id")
  nome=input("Nome:")
  cognome=input("Cognome")
  media_it=input("Media-ita: ")
  media_sci=input("media scienze")
  media_ing=input("media inglese:")
  studente=Student(id,nome,cognome,media_it,media_sci,media_ing)
  stringa_input=studente.stringa_stud()
  try:
     contenuto=lettura_file("database.csv")
  except:
     with open("database.csv","a") as data:
       data.write("id, nome, cognome, media italiano,media scienze, media inglese")
       contenuto=lettura_file("database.csv")
  righe=contenuto.split("\n")
  for i in range(1,len(righe)):
    lista_id.append(righe[i].split(",")[0])
  if id in lista_id:
     print("Studente già presente") 
  else:
    with open("database.csv","a") as data:
      data.write(stringa_input)
  chc=input("Vuoi inserire altro studente? (y,n)")
  if chc=='n':
    scelta='False'
