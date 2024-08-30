numeri1=[0,0,0,0,0]
numeri2=[0,0,0,0,0]
somma=[0,0,0,0,0]
print("Digitare i primi 5 numeri")
for i in range(5):
    q= int(input("Digita numero: "))
    numeri1[i]=q
print("Digitare altri 5 numeri")
for k in range(5):
    r= int(input("Digita numero: "))
    numeri2[k]=r
for z in range(5):
    somma[z]= numeri1[z]+numeri2[z]
print("L'array somma è:", somma)
