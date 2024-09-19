from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, RandomizedSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# Caricare il dataset wine
wine = load_wine()
X = wine.data  # Caratteristiche del vino
y = wine.target  # Etichette (tipi di vino)

# Creare la pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),            # Standardizza i dati
    ('pca', PCA()),                          # Riduce la dimensionalità
    ('gbc', GradientBoostingClassifier())    # GradientBoosting come classificatore
])

# Suddividere il dataset in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Definire la griglia di parametri per GradientBoostingClassifier
param_grid = {
    'gbc__max_depth': [3, 5, 7],          # Profondità massima degli alberi
    'gbc__n_estimators': [50, 100, 200],  # Numero di alberi nel modello
    'gbc__learning_rate': [0.01, 0.1, 0.2] # Rateo di apprendimento
}
stratified_kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Inizializzare RandomizedSearchCV, ottimizza gli iperparametri per trovare il modello migliore da utilizzare
random_search = RandomizedSearchCV(
     pipeline,               # La pipeline da ottimizzare
     param_distributions=param_grid,  # Griglia di parametri di GBC DA OTTIMIZZARE!
     n_iter=10,              # Numero di combinazioni casuali da provare, non tutte, a differenza di GridSearchCV
     cv=stratified_kfold,                  # Numero di fold per la cross-validation
     scoring='accuracy',
     random_state=42, 
     n_jobs=-1      
 )

# Eseguire la ricerca RandomizedSearchCV
random_search.fit(X_train, y_train)#prova i diversi metodi



# Migliori parametri trovati
print(f"Migliori parametri trovati: {random_search.best_params_}")


# Predizione sul test set
y_pred = random_search.predict(X_test)

# Report di classificazione
print("Report di classificazione:")
print(classification_report(y_test, y_pred))

# Matrice di confusione
print("Matrice di confusione:")
print(confusion_matrix(y_test, y_pred))

# Accuratezza
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza sul test set: {accuracy:.4f}")

