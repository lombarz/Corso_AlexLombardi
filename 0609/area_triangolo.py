def area_trinagolo(b,a):
    area=b*a/2
    return area
def area_rettangolo(b,a):
    area=b*a
    return area
def area_quadrato(l):
    area=l**2
    return area
def controllo(stop):
   chc2=input("Vuoi fare un'altra operazione? s n")
   if chc2=='n':
      stop='True'
   return stop
   

stop='False'
while stop=='False':
 chc=int(input("Di che oggetto vuoi calcolare l'area? 1=triangolo, 2=rettangolo, 3=quadrato"))
 if chc==1:
   altezza=int(input("valore altezza: "))
   base=int(input("valore altezza: "))
   output= area_trinagolo(base,altezza)
   print("L'area è ", output)
   controllo(stop)
 elif chc==2:
   altezza=int(input("valore altezza: "))
   base=int(input("valore altezza: "))
   output= area_rettangolo(base,altezza)
   print("L'area è ", output)
   controllo(stop)
 elif chc==3:
   lato=int(input("valore lato: "))
   output= area_quadrato(lato)
   print("L'area è ", output)
   controllo(stop)
 else:
    print("Valore errate, ripetere selezione")