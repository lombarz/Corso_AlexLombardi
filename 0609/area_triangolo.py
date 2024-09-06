def area_trinagolo():
    altezza=int(input("valore altezza: "))
    base=int(input("valore altezza: "))
    area=base*altezza/2
    print("l'area vale", area)
def area_rettangolo():
    altezza=int(input("valore altezza: "))
    base=int(input("valore altezza: "))
    area=base*altezza
    print("l'area vale", area)
def area_quadrato():
    lato=int(input("valore lato: "))
    area=lato**2
    print("l'area vale", area)
def controllo():
   chc2=input("Vuoi fare un'altra operazione? s n")
   if chc2=='n':
    return 'True'
   else:
    return 'False'
   

stop='False'
while stop=='False':
 chc=int(input("Di che oggetto vuoi calcolare l'area? 1=triangolo, 2=rettangolo, 3=quadrato"))
 if chc==1:
   area_trinagolo()
 elif chc==2:
   area_rettangolo()
 elif chc==3:
   area_quadrato()
 else:
    print("Valore errato")
 stop=controllo()