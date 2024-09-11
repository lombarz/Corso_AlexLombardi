""" Crea una classe chiamata Punto. Questa classe dovrebbe avere:
Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le
coordinate del punto di questi valori.
Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del
piano. """

from math import sqrt #importo il metodo per le radici
class Punto:
    def __init__(self, x, y):#costruttore
        if type (x) is float and type (y)is float:#controllo tipo
            self.x= x
            self.y= y
        else:
            print("dati non validi")
    def muovi (self, dx, dy):#sposta le coordinate di punto
        if type (dx)is float and type (dy)is float:
            try:
              self.x+=dx 
              self.y+=dy
              return self
            except:
              print("operazione non valida")
        else:
               print("spostamenti devono essere numeri")
    def distanza_da_origine(self):#calcola la distanza dal centro
        try:#controllo tipo
          dist=sqrt((self.x)**2+(self.y)**2)
          return dist
        except:
            print("operazione non eseguibile")
        
punto1= Punto("a",2)
if type(punto1==Punto):
  try:
   punto1= punto1.muovi(1,1)
   distanza1= punto1.distanza_da_origine()
   print(f"Il punto è",{punto1.x,punto1.y},"con distanza", distanza1)
  except:
     print("annullamento operazione")
#non funziona benissimo