from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import adjusted_rand_score, homogeneity_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

iris=load_iris()
X = iris.data#qui sto già prendendo tutte le quattro caratteristiche
y = iris.target

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42)

# Addestrare il modello e predire i cluster
kmeans.fit(X_scaled)
clusters = kmeans.predict(X_scaled)

# 3. Ridurre la dimensionalità con PCA per visualizzare i cluster su un piano 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Creare un DataFrame per visualizzare i risultati
df = pd.DataFrame(X_pca, columns=['PCA1', 'PCA2'])
df['Cluster'] = clusters
df['True Label'] = y
print(df)
# 4. Confronto con le etichette reali e valutazione del clustering
# Calcolare l'Adjusted Rand Index
ari = adjusted_rand_score(y, clusters)
print(f'Adjusted Rand Index: {ari:.2f}')

# Calcolare l'Homogeneity Score
homogeneity = homogeneity_score(y, clusters)
print(f'Homogeneity Score: {homogeneity:.2f}')

# 5. Visualizzare i veri gruppi
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='True Label', palette='Set1', s=100, alpha=0.7, marker='o')
plt.title(' Speci di iris divise con Clustering(ridotto a 2D con PCA)')
plt.xlabel('Prima Componente Principale')
plt.ylabel('Seconda Componente Principale')
plt.show()

# 6. Visualizzare i cluster con un grafico 2D delle prime due componenti principali
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='Set1', s=100, alpha=0.7, marker='o')
plt.title('K-Means Clustering su Iris (ridotto a 2D con PCA)')
plt.xlabel('Prima Componente Principale')
plt.ylabel('Seconda Componente Principale')
plt.show()

