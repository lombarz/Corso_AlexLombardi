class Automobile:
    numero_ruote=4 #attributo di classe
    def __init__(self, marca, modello):#metodo COSTRUTTORE
        self.marca= marca#attributo di istanza
        self.modello=modello#attributo di istanza
    def stampa_info(self):# metodo di istanza
        print("L'automobile è una ", self.marca, self.modello)

auto1= Automobile("Fiat", "500")
auto2= Automobile("BMW", "X3")
auto1.stampa_info()
auto2.stampa_info()