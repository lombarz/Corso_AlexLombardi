from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

digits=load_digits()
X=digits.data
y=digits.target
df = pd.DataFrame(X, columns=digits.feature_names)
print(df)


pca = PCA(n_components=2,random_state=42)
X_pca = pca.fit_transform(X)

# Creare un DataFrame per visualizzare i risultati
df_pca = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
df_pca['Target'] = y

print(df_pca)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_pca, x='PCA1', y='PCA2', hue='Target', palette='Set1', s=100, alpha=0.7, marker='o')
plt.title(' Digits ridotto a 2D con PCA')
plt.xlabel('Prima Componente Principale')
plt.ylabel('Seconda Componente Principale')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
svc = SVC(kernel='linear', C=1.0, random_state=42)  # Puoi usare altri kernel come 'rbf', 'poly', ecc.

# 5. Addestrare il modello
svc.fit(X_train, y_train)

# 6. Fare previsioni sul test set
y_pred = svc.predict(X_test)

# 7. Valutare le prestazioni del modello
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuratezza: {accuracy:.2f}')
#ripeto l'analisi con pca
X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y, test_size=0.3, random_state=42)

# 5. Addestrare il modello
svc.fit(X_train_pca, y_train_pca)

# 6. Fare previsioni sul test set
y_pred_pca = svc.predict(X_test_pca)

# 7. Valutare le prestazioni del modello dopo pca
accuracy_pca = accuracy_score(y_test_pca, y_pred_pca)
print(f'Accuratezza: {accuracy_pca:.2f}')
if accuracy>accuracy_pca:
    print("La PCA ha ridotto l'accuratezza")
elif accuracy<accuracy_pca:
    print("La PCA ha aumentato l'accuratezza")
else:
    print("La PCA non ha cambiato l'accuratezza")