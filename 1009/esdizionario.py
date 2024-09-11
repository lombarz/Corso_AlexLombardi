""" Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2} """

stringa=input("Inserisci stringa: ")
dizionario={}
for elemento in stringa:# conto il numero di elementi uguali presenti nella stringa per tipo
    """ if elemento in dizionario:
      dizionario[elemento]+=1
    else: """
    n=stringa.count(elemento)#maggior efficienza, codice ispirato da Martina
    dizionario.setdefault(elemento,n)
print(dizionario)

lista_valori=list(dizionario.values())
lista_chiavi=list(dizionario.keys())
dizionario2=dict(zip(lista_valori,lista_chiavi))#creo un dizionario dove inverto valori e chiavi!
dizionario3={}
for element in sorted(dizionario2, reverse=True):#ordino per la nuova chiave, cioè i valori del primo dizionario, in ordine decrescente
    dizionario3[dizionario2[element]]=element#inverto nuovamente chiavi e valori per stamparlo nell'ordine del primo dizionario!
print("Dizionario3:",dizionario3)
dizionario4={dizionario2[element]:element for element in sorted(dizionario2, reverse=True) }
print("Dizionario4:",dizionario4)