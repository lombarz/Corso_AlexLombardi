from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def grafico_calore(dati,matrice):
#Grafico matrice di confusione (molto bello)
  plt.figure(figsize=(8, 6))
  sns.heatmap(matrice, annot=True, fmt='d', cmap='Blues', xticklabels=dati.target_names, yticklabels=dati.target_names)#heatmap
  plt.xlabel('Classe Predetta')
  plt.ylabel('Classe Reale')
  plt.title('Matrice di Confusione')
  plt.show()

def confronto_modelli(model1,model2,data,data_name):
  print(f"Benvenuto, confrontiamo i riultati del modello {model1} con quelli del modello {model2} per il dataset {data_name}")
  X = data.data  # Caratteristiche (lunghezza e larghezza di sepali e petali)
  y = data.target  # Etichette (specie di Iris)
#print(X)
  scaler=StandardScaler()
  X_scaled=scaler.fit_transform(X)#normalizzare e ridimensiore i dati prima  di applicare algoritmi di ML
#print(X_scaled)
  X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
  scores_1 = cross_val_score(model1, X_scaled, y, cv=5)
  scores_2 = cross_val_score(model1, X_scaled, y, cv=5)
# Mostriamo i punteggi per ciascun fold
  print(f"Risultati {model1}:\n")
  print("Punteggi per ciascun fold:", scores_1)
# Mostriamo la media e la deviazione standard dei punteggi
  print("Media dei punteggi: %.2f" % scores_1.mean())
  print("Deviazione standard dei punteggi: %.2f" % scores_1.std())
  dtc.fit(X_train,y_train)#il fit serve per fare il training del modello
  predictions=dtc.predict(X_test)#qui facciamo le predizione dei dati lasciati i test
  print(f"Classification Report {model1}:\n", classification_report(y_test, predictions, target_names= data.target_names))#divide l'accuratezze per specifiche classi
  cm1 = confusion_matrix(y_test, predictions)#dice,per ogni classe, quante volte è stat confusa e con quali altre classi
  print(f"Matrice di confusione {model1}\n",cm1)
  grafico_calore(data,cm1)
  print(f"Risultati {model2}:\n")
  print("Punteggi per ciascun fold:", scores_2)
# Mostriamo la media e la deviazione standard dei punteggi
  print("Media dei punteggi: %.2f" % scores_2.mean())
  print("Deviazione standard dei punteggi: %.2f" % scores_2.std())
  dtc.fit(X_train,y_train)#il fit serve per fare il training del modello
  predictions=dtc.predict(X_test)#qui facciamo le predizione dei dati lasciati i test
  print(f"Classification Report {model2}:\n", classification_report(y_test, predictions, target_names= data.target_names))#divide l'accuratezze per specifiche classi
  cm2 = confusion_matrix(y_test, predictions)#dice,per ogni classe, quante volte è stat confusa e con quali altre classi
  print(f"Matrice di confusione {model2}\n",cm2)
  grafico_calore(data,cm2)




# # Suddividere il dataset in set di training e test
vino = load_wine()
nome_data='Wine'
knn=KNeighborsClassifier(n_neighbors=5)
dtc=DecisionTreeClassifier()#DTC,usato per classificazioni
confronto_modelli(knn,dtc,vino,nome_data)
    
      