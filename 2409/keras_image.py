import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, classification_report

# Caricamento del dataset MNIST
(X_train, y_train), (X_test, y_test) = mnist.load_data()
#normalizzazione dei dati per le possibili scale di grigio di un pixel (255)
X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255
# Convertire le etichette in linguaggio macchina (vettori->one-hot)
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)
#creazione del modello sequenziale
model=Sequential()
model.add(Flatten(input_shape=(28, 28)))# Appiattire le immagini 28x28 in vettori di 784 elementi
model.add(Dense(64,activation='relu',input_dim=100))#hidden layers/layer iniziale input_dim
model.add(Dense(10,activation='softmax'))#strato finale
#compilazione con ottimizzatore, funzione di perdita e accurancy
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
#summary del modello
model.summary()
#addestramento
model.fit(X_train,y_train,
          epochs=5,
          batch_size=32,#addestra 32 volte una relazione, se true crea un nodo e un peso 32(=0.1)
          validation_split=0.1)
#valutazione delle prestazioni
test_loss,test_acc=model.evaluate(X_test,y_test,batch_size=128)#batch_size=128 specifica il numero di campioni da utilizzare in ciascun sottoinsieme (batch) durante la valutazione del modello sui dati di test.
print(f'Accuratezza sul set di test:{test_acc},\n Loss:{test_loss}')
#predictions
predictions=model.predict(X_test)
predicted_classes = np.argmax(predictions, axis=1)#mi da la singola classe più probabile
true_classes = np.argmax(y_test, axis=1)

# Matrice di confusione
conf_matrix = confusion_matrix(true_classes, predicted_classes)
plt.figure(figsize=(10,8))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.title('Matrice di Confusione')
plt.xlabel('Classe Predetta')
plt.ylabel('Classe Vera')
plt.show()

# Report di classificazione
report = classification_report(true_classes, predicted_classes)
print('Report di Classificazione:')
print(report)

# Visualizzazione di alcune predizioni
num_images = 5
random_indices = np.random.choice(len(X_test), num_images)
plt.figure(figsize=(15,3))
for i, idx in enumerate(random_indices):
    image = X_test[idx].reshape(28, 28)
    true_label = true_classes[idx]
    predicted_label = predicted_classes[idx]
    
    plt.subplot(1, num_images, i+1)
    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.title(f'T:{true_label}, P:{predicted_label}')
plt.show()