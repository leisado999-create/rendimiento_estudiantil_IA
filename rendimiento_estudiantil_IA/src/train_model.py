import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Simulación de datos
np.random.seed(42)
df = pd.DataFrame({
    "horas_estudio": np.random.randint(1, 20, 50),
    "asistencia": np.random.randint(60, 100, 50),
    "participacion": np.random.randint(1, 10, 50)
})
df["promedio_final"] = (
    0.5*df["horas_estudio"] +
    0.3*(df["asistencia"]/10) +
    0.7*df["participacion"] +
    np.random.randn(50)
)

# División del dataset
X = df[["horas_estudio", "asistencia", "participacion"]]
y = df["promedio_final"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Entrenamiento del modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Guardar modelo
joblib.dump(model, "modelo.pkl")

print("✅ Modelo entrenado y guardado como modelo.pkl")
