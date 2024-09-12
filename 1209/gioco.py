import random

def vuoi_proseguire():
    choice = input("vuoi proseguire? (y/n)")
    return choice



numeri_casuali = random.sample(range(1, 100), 5)

#print(numeri_casuali)

numeri_casuali2 = []
for i in numeri_casuali:
    numeri_casuali2.append(str(i))
    
#print(numeri_casuali2)
    

with open("numeri.csv","w") as file:
    file.write(','.join(numeri_casuali2))
        
  
    
with open("numeri.csv","r") as file:
    lista = file.read()

lista_numerica = lista.split(',')

#print(lista_numerica)
count=0
n="y"
for i in range(3):
    numero1 = input("Inserisci numero 1 : ")
    numero2 = input("Inserisci numero 2 : ")
    
    if numero1 in lista_numerica and numero2 in lista_numerica:
        print("Hai indovinato")
        break
    elif numero1 in lista_numerica:
        print(f"Hai indovinato solo {numero1}")
        count+=1
        if i<2:
            n = vuoi_proseguire()
            if n == 'n':
               break
    elif numero2 in lista_numerica:
        print(f"Hai indovinato solo {numero2}")
        count+=1
        if i<2:
            n = vuoi_proseguire()
            if n == 'n':
               break
    else:
        print("Non hai indovinato")
        count+=1
        if i<2:
            n = vuoi_proseguire()
            if n == 'n':
               break
if n=='n' or count==3:
    print("GAME OVER")

        