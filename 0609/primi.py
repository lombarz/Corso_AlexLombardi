   
def decoratoreprimo(funzione):
   def primo_o_no():
    nome=funzione()
    numeri=[]
    stop='False'
    prime='True'
    while stop=='False':
       q=int(input("Digita un numero: "))
       if q> 1: 
         for i in range(2, int(q / 2) + 1):
           if (q % i) == 0:
            print("Non è un primo, divisore più piccolo= ",i)
            prime='False'
            break
            #return 'False'
         if prime=='True':
           numeri.append(q)
             #return 'True'
       else:
         prime='False'
       chc2=input("Vuoi fare un'altra operazione? s n")
       if chc2=='n':
         stop='True'
    print(numeri)
    return nome
   return primo_o_no
      
@decoratoreprimo     
def richiesta_nome():
  nome=input("Qual'è il tuo nome? ")
  return nome

print ("Ciao ",richiesta_nome())