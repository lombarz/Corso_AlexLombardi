from es2_classe_libro import Libro

class Biblioteca:
    archivio=[]
    def aggiungi_libro(self,libro):
        if type(libro)is Libro:
          try:
            self.archivio.append(libro)
          except:
            print("Errore sconosciuto")
        else:
            print("Le biblioteche hanno solo libri!")
    def mostra_archivio(self):
        for libro in self.archivio:
            libro.descrizione()
    


biblioteca1 = Biblioteca()#come inizializzazione lista (vuota)
while True:
    mod = int(input('Cosa vuoi fare? 1.Aggiungere libro Libro 2.Mostra Archivio 3.Esci'))
    if mod == 1:
        titolo = input('Inserisci titolo: ')
        autore = input('inserisci autore: ')
        pagine = int(input('Inserisci numero pagine: '))
        book= Libro(titolo,autore,pagine)
        biblioteca1.aggiungi_libro(book)
    elif mod == 2:
        biblioteca1.mostra_archivio()
    elif mod == 3:
        break
    else:
        print('Scelta non valida')


