def menu():
    ciclo='True'
    while ciclo=='True':
      richiesta= input("Cosa vuoi fare? a=vedere argomento, b=lista argomenti selezionabili")
      if richiesta=='b':
        print("Lista argomenti: 1=UML, 2= Cicli, 3=Liste, 4=Metodologie, 5=Taskig, 6=IDE, 7=Ruoli Aziendali, 8=GITHUB, 9=Range, 10=Condizioni")
      elif richiesta=='a':
        argomento=int(input("Inserisci il numero dell'argomento da approfondire: "))
        if argomento== 1:
          UML()
        elif argomento==2:
          cicli()
        elif argomento==3:
          liste()
        elif argomento==4:
          metodologie()
      else:
        print("Selezione sbagliata! Ripetere")
      chc=input("Vuoi tornare alla home? s n")
      if chc=='n':
        ciclo='False'
    
def UML():
  print("UML(Unified Modeling Lenguage) è un metodo standardizzato, visuale, polivalente ed estensibile per la rappresentazione grafica di un processo e/o softwere")
def cicli():
   print("I cicli sono strumenti che permettono di eseguire in maniera ripetuta un codice, i casi visti sono 'while', che può ripetersi all'infinito finchè l'utente non compie un'azione che lo blocchi, e 'for', che invece si ripete per un numero prestabilito di volte")
   print("Ecco un esempio di while: while 3<=i<=100 : print(i); i=i/2") 
   i=100
   while 3<=i<=100 :
    print(i)
    i=i/2
   print("Ecco un esempio di for:q= int(input(Scegli un numero: ));for num in range(q,-1,-1):print(num)")
   q= int(input("Scegli un numero: "))
   for num in range(q,-1,-1):
     print(num)
def liste():
  print("Le liste sono un tipo di dati che permette di inserire tipi di dati diversi e di indicizzarli, ecco un esempio di lista")
  lista=[1,2,3,4,5,"pippo",'True', 11.97]
  print(lista)
def metodologie():
  print("Le metodologie di sviluppo softwere principali sono Waterfall, più rigida e gerarchizzata, e Agile, più libera e coinvolgente")



menu()