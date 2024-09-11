class Prodotti:
    def __init__(self,nome,costo_produzione,prezzo_vendita):
        self.nome=nome
        self.costo_produzione=costo_produzione
        self.prezzo_vendita=prezzo_vendita
    def calcola_profitto(self):
        profitto=self.prezzo_vendita-self.costo_produzione
        return profitto

class Strumenti(Prodotti):
    def __init__(self,nome,costo_produzione,prezzo_vendita,tipo_strumento,casa_produttrice,anno_produzione):
        Prodotti.__init__(self,nome,costo_produzione,prezzo_vendita)
        """ self.nome=nome
        self.costo_produzione=costo_produzione
        self.prezzo_vendita=prezzo_vendita """
        self.tipo_strumento=tipo_strumento
        self.casa_produttrice=casa_produttrice
        self.anno_produzione=anno_produzione

class Dischi(Prodotti):
    def __init__(self,nome,costo_produzione,prezzo_vendita,artista,etichetta,tipo_supporto):
        Prodotti.__init__(self,nome,costo_produzione,prezzo_vendita)
        """ self.nome=nome
        self.costo_produzione=costo_produzione
        self.prezzo_vendita=prezzo_vendita """
        self.artista=artista
        self.etichetta=etichetta
        self.tipo_supporto=tipo_supporto
    
class Fabbrica_Musica:
    def __init__(self):
        self.inventario={}
        self.saldo=0
    def aggiungi_prodotto(self,prodotto):
        print("Stai aggiungendo ",prodotto.nome, "al tuo catalogo")
        self.inventario.setdefault(prodotto.nome,0)
        quantità=int(input("Quantità:"))
        self.inventario[prodotto.nome]+=quantità
    def resi_prodotto(self,prodotto):
        print("Stai rendendo ",prodotto.nome)
        resi=int(input("Quanti prodotti sono stati resi? "))
        if prodotto.nome in self.inventario.keys():
          self.inventario[prodotto.nome]+=resi
          perdita=resi*prodotto.calcola_profitto()
          print("Soldi restituiti=",perdita)
          self.saldo-=perdita
        else:
          print("Il prodotto non era presente in inventario")#se lo era prima, la quantità sarebbe zero
    def vendi_prodotto(self,prodotto):
        if prodotto.nome in self.inventario.keys():
          print("Stai vendendo ",prodotto.nome)
          venduti=int(input("Numero prodotti venduti: "))
          if venduti<=self.inventario[prodotto.nome]:
                  guadagno=venduti*prodotto.calcola_profitto()
                  self.inventario[prodotto.nome]-=venduti
                  print("Il guadagno della vendita è stato ",guadagno)
                  self.saldo+=guadagno
          else:
                print("Prodotto insufficiente")
        else:
            print("Prodotto inesistente")
    def mostra_inventario(self):
        print(self.inventario)
    def saldo_attaule(self):
        print("Il saldo attuale è ", self.saldo)
        chc=input("Azzerare giornata corrente? s, n")
        if chc=='s':
            self.saldo=0
            print("Giornata finita, saldo attuale azzerato")
            return 'False'
        else:
            print("Buon lavoro")
            return 'True'
           

ciclo='True'
while ciclo=='True':
  catalogo=Fabbrica_Musica()
  asdfg = Strumenti('asdfg', 200, 400, 'chitarra','yamaha','2012')
  asdfg_2000 = Strumenti('asdfg_2000', 180, 350, 'basso','yamaha','2012')
  all_hope_is_gone = Dischi('all hope is gone', 10, 20, 'Slipknot', 'Sony','cd')
  nevermind = Dischi('nevermind', 5, 15, 'Nirvana', 'Universal','vinile')
  catalogo.aggiungi_prodotto(asdfg)
  catalogo.aggiungi_prodotto(asdfg_2000)
  catalogo.aggiungi_prodotto(all_hope_is_gone)
  catalogo.aggiungi_prodotto(nevermind)
  catalogo.mostra_inventario()
  catalogo.vendi_prodotto(nevermind)
  catalogo.vendi_prodotto(asdfg_2000)
  catalogo.resi_prodotto(asdfg)
  catalogo.resi_prodotto(all_hope_is_gone)
  catalogo.mostra_inventario()
  ciclo=catalogo.saldo_attaule()

""" while 'True':
    ciclo=input("Nuova operazione? s,n")
    if ciclo=='s':
     chc=int(input("Cosa vuoi fare? Aggiungere nuovo prodotto 1, Vendere Prodotto 2, Reso Prodotto 3"))
     if chc==1:
        nome=input("Nome: ")
        costo_produzione=float(input("Costo produzione "))
        prezzo=float(input("prezzo "))
        tipo=int(input("E' uno strumento(=1) o un disco(=2)?"))
        if tipo==1:
            tipo_strumento=input("Tipo strumento: ")
            casa_prod=input("Casa produttrice: ")
            anno=int(input("anno: "))
            strumento=Strumenti(nome,costo_produzione,prezzo,tipo_strumento,casa_prod,anno)
            catalogo.aggiungi_prodotto(strumento)
        else:
            artista=input("artista")
            etichetta=input("etichetta")
            supporto=input("Tipo supporto")
            disco=Dischi(nome,costo_produzione,prezzo,artista,etichetta,supporto)
            catalogo.aggiungi_prodotto(disco)
     elif chc==2:
          prodotto_nome=input("Quale prodotto vuoi vendere? ")
          if prodotto_nome in catalogo.keys():
              venduti=int(input("Numero vendite: "))
              if venduti<=catalogo[prodotto_nome]:
                  catalogo.vendi_prodotto(prodotto,venduti)
              else:
                print("Prodotto insufficiente")
          else:
              print("Prodotto non presente")
     elif chc==3:
        prodotto=input("Quale prodotto vuoi rendere? ")
        resi=int(input("Numero resi: "))
        catalogo.resi_prodotto(prodotto,resi)
     else:
         print("Operazione non ammessa")
         continue
    else:
        break """


