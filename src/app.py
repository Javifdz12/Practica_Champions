from flask import Flask, render_template
from dotenv import load_dotenv
import os
from config.mongodb import mongo
from tensorflow.keras.models import load_model
import joblib
import pandas as pd

preprocessor = joblib.load('preprocessor.pkl')
model = load_model('Pesos_Champions.best.hdf5')

def mapear_a_rango(y):
    if y < 1:
        y = 1
    elif y > 50:
        y = 50
    nuevo_valor = 1 + ((y - 1) * 9) / 49
    return round(nuevo_valor, 2)

def obtener_probabilidades_y_cuotas():
    # Asegúrate de excluir el '_id' cuando recuperas los datos
    partidos = mongo.db.Champions.find({}, {'_id': False})
    partidos_df = pd.DataFrame(list(partidos))

    # Aplicar transformaciones
    partidos_transformados = pd.DataFrame(preprocessor.transform(partidos_df))

    # Predecir probabilidades
    prob = model.predict(partidos_transformados)

    # Calcular cuotas
    cuotas_local = [1/x[0]*0.9 for x in prob]
    cuotas_visitante = [1/x[2]*0.9 for x in prob]
    cuotas_empate = [1/x[1]*0.9 for x in prob]

    return cuotas_local, cuotas_empate, cuotas_visitante


load_dotenv() 

app = Flask(__name__)

app.config['MONGO_URI']=os.getenv('MONGO_URI')
mongo.init_app(app)

@app.route('/')
def index():
    partidos = mongo.db.Champions.find()
    partidos_lista = [partido for partido in partidos]  # Convertir cursor a lista
    cuotas_local, cuotas_empate, cuotas_visitante = obtener_probabilidades_y_cuotas()

    # Combinar datos de partidos con cuotas
    for i, partido in enumerate(partidos_lista):
        partido['cuota_local'] = mapear_a_rango(cuotas_local[i])
        partido['cuota_empate'] = mapear_a_rango(cuotas_empate[i])
        partido['cuota_visitante'] = mapear_a_rango(cuotas_visitante[i])

    return render_template('index.html', partidos=partidos_lista)

if __name__ == '__main__':
	app.run(debug=True)
