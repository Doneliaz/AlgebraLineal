import pandas as pd
import numpy as np

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Preprocesado y modelado
# ==============================================================================
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Configuración matplotlib
# ==============================================================================
plt.rcParams['image.cmap'] = "bwr"
#plt.rcParams['figure.dpi'] = "100"
plt.rcParams['savefig.bbox'] = "tight"
style.use('ggplot') or plt.style.use('ggplot')

# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

path_to_file = 'C:/Users/celso/Python310/student_scores.csv'
datos = pd.read_csv(path_to_file)
print(datos.head(3))

#equipos = ["Texas","Boston","Detroit","Kansas","St.","New_S.","New_Y.",
#           "Milwaukee","Colorado","Houston","Baltimore","Los_An.","Chicago",
#           "Cincinnati","Los_P.","Philadelphia","Chicago","Cleveland","Arizona",
#           "Toronto","Minnesota","Florida","Pittsburgh","Oakland","Tampa",
#           "Atlanta","Washington","San.F","San.I","Seattle"]
#bateos = [5659,  5710, 5563, 5672, 5532, 5600, 5518, 5447, 5544, 5598,
#          5585, 5436, 5549, 5612, 5513, 5579, 5502, 5509, 5421, 5559,
#          5487, 5508, 5421, 5452, 5436, 5528, 5441, 5486, 5417, 5421]

#runs = [795, 775, 787, 730, 762, 718, 767, 721, 735, 615, 708, 644, 654, 735,
#        667, 713, 654, 704, 731, 743, 619, 625, 610, 645, 707, 641, 624, 670,
#        643, 656]

#datos = pd.DataFrame({'equipos': equipos, 'bateos': bateos, 'runs': runs})
#print(datos.head(3))

# Gráfico
# ==============================================================================
fig, ax = plt.subplots(figsize=(6, 3.84))

datos.plot(
    x    = 'Horas',
    y    = 'Resultados',
    c    = 'firebrick',
    kind = "scatter",
    ax   = ax
)
#ax.set_title('Distribución de bateos y runs');
ax.set_title('Horas Estudio vs Resultados');
plt.show()

#corr_test = pearsonr(x = datos['bateos'], y =  datos['runs'])
corr_test = pearsonr(x = datos['Horas'], y =  datos['Resultados'])
print("\n Coeficiente de correlación de Pearson: ", corr_test[0])
print("P-value: ", corr_test[1])

#X = datos[['bateos']]
#y = datos['runs']
X = datos[['Horas']]
y = datos['Resultados']
X_train, X_test, y_train, y_test = train_test_split(
                                        X.values.reshape(-1,1),
                                        y.values.reshape(-1,1),
                                        train_size   = 0.8,
                                        random_state = 1234,
                                        shuffle      = True
                                    )

# Creación del modelo
# ==============================================================================
modelo = LinearRegression()
modelo.fit(X = X_train.reshape(-1, 1), y = y_train)

print("\n Intercept:", modelo.intercept_)
print("Coeficiente:", list(zip(X.columns, modelo.coef_.flatten(), )))
print("Coeficiente de determinación R^2:", modelo.score(X, y))

predicciones = modelo.predict(X = X_test)
print(predicciones[0:3,])

rmse = mean_squared_error(
        y_true  = y_test,
        y_pred  = predicciones,
        squared = False
       )
print("")
print(f"El error (rmse) de test es: {rmse}")

# División de los datos en train y test (Statsmodels)
# ==============================================================================
X = datos[['Horas']]
y = datos['Resultados']

X_train, X_test, y_train, y_test = train_test_split(
                                        X.values.reshape(-1,1),
                                        y.values.reshape(-1,1),
                                        train_size   = 0.8,
                                        random_state = 1234,
                                        shuffle      = True
                                    )

X_train = sm.add_constant(X_train, prepend=True)
modelo = sm.OLS(endog=y_train, exog=X_train,)
modelo = modelo.fit()
print('\n', modelo.summary())

# Intervalos de confianza para los coeficientes del modelo
# ==============================================================================
print(modelo.conf_int(alpha=0.05))

# Predicciones con intervalo de confianza del 95%
# ==============================================================================
predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
print(predicciones.head(4))

predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
predicciones['x'] = X_train[:, 1]
predicciones['y'] = y_train
predicciones = predicciones.sort_values('x')
print(predicciones.head(3))

# Gráfico del modelo
# ==============================================================================
fig, ax = plt.subplots(figsize=(6, 3.84))

ax.scatter(predicciones['x'], predicciones['y'], marker='o', color = "gray")
ax.plot(predicciones['x'], predicciones["mean"], linestyle='-', label="OLS")
ax.plot(predicciones['x'], predicciones["mean_ci_lower"], linestyle='--', color='red', label="95% CI")
ax.plot(predicciones['x'], predicciones["mean_ci_upper"], linestyle='--', color='red')
ax.fill_between(predicciones['x'], predicciones["mean_ci_lower"], predicciones["mean_ci_upper"], alpha=0.1)
ax.legend();
plt.show()
