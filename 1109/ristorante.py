class Ristorante:
    def __init__(self, nome_ristorante, tipo_cucina):
        self.nome=nome_ristorante
        self.tipo= tipo_cucina
        self.aperto="False"
        self.menu={"test":0}
    def descrivi_ristorante(self):
        print("Il ristorante ",self.nome," è un ristorante di cucina ",self.tipo)
    def stato_apertura(self):
        if self.aperto=="False":
          print("Il ristorante è chiuso")
        else:
          print("Il ristorante è aperto")
    def apertura_ristorante(self):
        self.aperto="True"
        print("Il ristorante ha aperto ora")
    def chiusura_ristorante(self):
        self.aperto="False"
        print("Il ristorante ha chiuso ora")
    def aggiungi_al_menu(self):
        self.menu.pop("test")
        while 'True':
            chc=input("Vuoi aggiungere una pietanza? s n")
            if chc=='s':
                pietanza=input("Nome pietanza: ")
                prezzo= float(input("Prezzo: "))
                self.menu[pietanza]=prezzo
            else:
                break
    def togli_dal_menu(self):
        while 'True':
            chc=input("Vuoi togliere una pietanza? s n")
            if chc=='s':
                pietanza=input("Nome pietanza: ")
                if pietanza in self.menu.keys():
                  self.menu.pop(pietanza)
                else:
                  print("Pietanza non presente")
            else:
                break
    def stampa_menu(self):
        print("Il menù del ristorante ",self.nome, " è:", self.menu)
    


nome=input("nome: ")
tipo=input("tipo cucina: ")
risto=Ristorante(nome,tipo)
risto.descrivi_ristorante()
risto.stato_apertura()
risto.apertura_ristorante()
risto.stato_apertura()
risto.chiusura_ristorante()
risto.stato_apertura()
risto.aggiungi_al_menu()
risto.togli_dal_menu()
risto.stampa_menu()
    
    