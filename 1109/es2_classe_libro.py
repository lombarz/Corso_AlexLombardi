""" Crea una classe chiamata Libro. Questa classe dovrebbe avere:
Tre attributi: titolo, autore e pagine.
Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto
da 'autore' e ha 'pagine' pagine.". """

class Libro:
    def __init__(self, titolo, autore, pagine):#costruttore
        if type (titolo) is str and type (autore) is str and type (pagine) is int:#controllo tipo
          self.titolo= titolo
          self.autore= autore
          self.pagine=pagine
        elif type (pagine!=int):
           print("Pagine deve avere un numero (intero)")
        else:
           print("Dati errati")
    def descrizione(self):#metodo per stampare info
       try:
         print("Il libro ",self.titolo," scritto da ",self.autore, " ha ",self.pagine, "pagine")
       except:
          print("Operazione non valida")

libro_tedesco=Libro("Mein Kampf","Adolf Hitler",666)
libro_tedesco.descrizione()