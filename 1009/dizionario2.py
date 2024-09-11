""" Scrivete un programma che chiede un numero all’utente e
restituisce un dizionario con il quadrato del numero, se è pari o
dispari e quante cifre contiene.
Esempio:
Numero 12
Risultato
{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 } """

num=int(input("Inserisci un numero:"))
dizionum={"quadrato":num**2}
if num%2==0:
  dizionum["pari o dispari"]="pari"
else:
  dizionum["pari o dispari"]="dispari"
parola=str(num)
cifra=len(parola)
dizionum["cifre"]=cifra
print(dizionum)
