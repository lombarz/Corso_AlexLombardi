""" Scrivete un programma che riceve in input una stringa lunga e verifica se ci sono duplicati, 
quanti sono, quali sono e quanto sono lunghi i duplicati. """

def contatore(paragrafo):
    paragrafo2=""
    for carattere in paragrafo:
       if carattere.isalpha() or carattere==" ":
          paragrafo2+=carattere      
    listone=paragrafo2.split(" ")
    listino={}
    result='False'
    for elemento in listone:
        if elemento.isalpha():
          listino[elemento]=listone.count(elemento)
    for numero in listino.values():
        if numero >1:
            result='True'
            break
    if result =='True':
      print("Il contatore dei caratteri è: ", listino)
    else:
      print("Non ci sono ripetizioni nel paragrafo ", paragrafo)

testo=input("inserisci il tuo testo: ")
contatore(testo)
    

    