from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns



# Caricare il dataset Iris
data = load_iris()
X = data.data  # Caratteristiche (lunghezza e larghezza di sepali e petali)
y = data.target  # Etichette (specie di Iris)

scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)#normalizzare e ridimensiore i dati prima  di applicare algoritmi di ML

# # Suddividere il dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

dtc=DecisionTreeClassifier()#DTC,usato per classificazioni
dtc.fit(X_train,y_train)#il fit serve per fare il training del modello
predictions=dtc.predict(X_test)#qui facciamo le predizione dei dati lasciati i test
print("Classification Report:\n", classification_report(y_test, predictions, target_names= data.target_names))#divide l'accuratezze per specifiche classi
cm = confusion_matrix(y_test, predictions)#dice,per ogni classe, quante volte è stat confusa e con quali altre classi
print("Matrice di confusione\n",cm)
#Grafico matrice di confusione (molto bello)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)#heatmap
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Reale')
plt.title('Matrice di Confusione')
plt.show()