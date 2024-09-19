from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
import matplotlib.pyplot as plt

diabete=load_diabetes()
X=diabete.data
y=diabete.target

df = pd.DataFrame(X, columns=diabete.feature_names)
df['Disease Progression'] = y

print(df.head())
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lr=LinearRegression()
lr.fit(X_train,y_train)
y_pred=lr.predict(X_test)
cv_scores = cross_val_score(lr, X, y, cv=5, scoring='neg_mean_squared_error')
# Calcolare MSE e R^2 score per la cross-validation
mse_scores = -cv_scores  # cross_val_score restituisce il negativo del MSE
mean_mse = mse_scores.mean()
std_mse = mse_scores.std()

print(f"Mean Cross-Validated MSE: {mean_mse:.2f}")
print(f"Standard Deviation of MSE: {std_mse:.2f}")

# Addestrare il modello sul set di addestramento e valutare su quello di test (opzionale)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Test Set Mean Squared Error: {mse:.2f}")
print(f"Test Set R^2 Score: {r2:.2f}")

# Visualizzare i risultati
plt.scatter(X_test[:, 0], y_test, color='blue', label='Dati reali')
plt.plot(X_test[:, 0], y_pred, color='red', linewidth=2, label='Retta di regressione')
plt.xlabel('Caratteristica')
plt.ylabel('Target')
plt.legend()
plt.show()

