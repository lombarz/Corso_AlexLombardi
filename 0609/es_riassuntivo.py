def controllore(funzione):#decoratore che funge da controllore per l'accesso al menù
   def involtino():
      answer='False'
      while answer=='False':
        nome=input("Controllo se puoi accedere al programma. Qual'è il nome (di battesimo) del docente di Python?")
        if nome==('mirko'or'Mirko'):#mirko se leggi questa cosa, non pensare sia uno psicopatico 
          print("Benvenuto!")
          answer='True'
        elif nome==('mirco'or'Mirco'):
          print("E' M-I-R-K-O, con la k! Comunque benvenuto!")
          answer='True'
        else:
          print("Mi spiace, accesso negato! (pss, era mirko...)")
      funzione()
   return involtino

      
def scelta_argomento(funzione):#decoratore che ti ricorda quale argomento hai scelto
  def primavera():
    print(f"Hai scelto l'argomento {funzione.__name__}, eccoti la spiegazione:")
    funzione()
  return primavera



@controllore
def menu():#menù, permette di vedere gli argomenti consultabile e di consultare l'argomento desiderato
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
        elif argomento==5:
          tasking()
        elif argomento==6:
          IDE()
        elif argomento==7:
          Ruoli_aziendali()
        elif argomento==8:
          GITHUB()
        elif argomento==9:
          rangef()
        elif argomento==10:
          condizioni()
        else:
          print(" Hai provato a fregarmi, ma io ero preparato! Non provare più a mandarmi in errore il codice!") 
      else:
        print("Selezione sbagliata!")
      chc=input("Vuoi tornare alla home? s n")
      if chc=='n':
        ciclo='False'
      elif chc=='s':
        ciclo='True'
      else:
        print("Non sai nemmeno spingere un tasto, per punzione ti riporto alla home!")
        ciclo='True'

@scelta_argomento   
def UML():
  print("UML(Unified Modeling Lenguage) è un metodo standardizzato, visuale, polivalente ed estensibile per la rappresentazione grafica di un processo e/o softwere")

@scelta_argomento
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

@scelta_argomento
def liste():
  print("Le liste sono un tipo di dati che permette di inserire tipi di dati diversi e di indicizzarli, ecco un esempio di lista")
  lista=[1,2,3,4,5,"pippo",'True', 11.97]
  print(lista)

@scelta_argomento
def metodologie():
  print("Le metodologie di sviluppo softwere principali sono Waterfall, più rigida e gerarchizzata, e Agile, più libera e coinvolgente")

@scelta_argomento
def tasking():
  print("Per tasking si intende la suddivisione dei compiti all'interno di un team per lo sviluppo di un progetto. Le metodologie con le quali può essere organizzato sono Waterfall e Agile")

@scelta_argomento
def IDE():
  print("IDE(Integrated development environment) sono ambienti di sviluppo integrato, applicazione che fornisce strumenti per lo sviluppo softwere")

@scelta_argomento
def Ruoli_aziendali():
  print("Abbiamo visto i vari ruoli aziendali che possono configurarsi nell'ambito tech, dal CEO al junior developer, con particolare attenzione a Business Analyst, Data Analyst e Data Scientist, nostre possibili occupazioni future")

@scelta_argomento
def GITHUB():
  print("GitHub è un servizio di hosting per progetti software, di proprietà della società GitHub Inc., con sede legale a San Francisco in California. Il nome deriva dal fatto che 'GitHub' è una implementazione dello strumento di controllo versione distribuito Git. Tra i molti soggetti che offrono servizi a livello internazionale che usano GitHub, le principali sono Google, Apple, Microsoft, NASA, Facebook, Twitter, Node.js, Ruby on Rails, JetBrains, JQuery, e GitHub stesso. (WIKI)")

@scelta_argomento
def rangef():
  print("range(start,stop,step) permette di creare un successione con inzio in start, passo step e fine in stop (non compreso), molto utile nei cicli for. Eccoti un esempio: ")
  start=int(input("Scrivi il tuo start (intero, mi raccomando!) "))
  stop=int(input("Scrivi il tuo stop (intero, mi raccomando!) "))
  step=int(input("Scrivi il tuo step (intero, te lo ripeto!) "))
  for x in range(start, stop, step):
    print(x)
  print("Visto? hai creato una successione con partenza in ", start,", passo ", step,", e fine ",stop," (non compreso,again!)")

@scelta_argomento
def condizioni():
  condition=input("Le condizioni servono per vedere casi diversi all'interno del codice, e vengono scritte attravero if/else/elif. Vuoi un esempio della loro applicazione? s n ")
  if condition=='s':
    print("(if) Eccolo, te l'ho appena fatto! Questo messaggio appare perche hai scelto sì")
  elif condition=='n':
    print("(elif) Peccato, te l'ho fatto lo stesso! Questo messaggio appare perche hai scelto no")
  else:
    print("(else) Hai provato a fregarmi, ma io ero preparato! Non provare più a mandarmi in errore il codice!")

menu()