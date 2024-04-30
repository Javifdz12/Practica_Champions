# CASA APUESTAS.

El siguiente repositorio corresponde a una API la cual he pusheado a este repositorio.
En ella hay una carpeta (src) la cual contine:
- Carpeta templates: que contiene el index.html.
- Carpeta config: que contiene archivo mongodb.py donde se ha inicializo PyMongo().
- Archivo app.py.
- Archivo Pesos_Champions.best.hdf5: que son los pesos del modelo que se ha entrenado para calcular en un partido la probabilidad de que gane el local, gane el visitante o empaten.
- Preprocessor.pkl: que son las transformaciones que se han aplicado a los datos para que puedan entrar en el modelo.
- Archivo requirements.txt: que contiene las librerias necesarias y sus versiones.

También contiene un .env que contiene el MONGO_URI correspondiente a mi cluster de mongodb, pero este no lo he añadido por temas de seguridad. Además la carpeta del venv tampoco la he añadido,
ya que era demasiado pesada para meterla en el repositorio.
En linux, para levantar la API hay que:
- Acceder a carpeta src: cd src
- Instalar entorno virtual: python -m venv venv
- Activar entorno virtual: source venv/bin/activate
- Instalar las dependecias: pip install -r requirements.txt
- Crear .env con MONGO_URI en su interior: MONGO_URI="aqui va tu MONGO_URI"
- Ejecutar archivo app.py: python3 app.py o también python app.py
Ahora deberias ver la API desplegada en 127.0.0.1:5000 (al menos a mi se me despliega ahí, en tu caso deberás comprobar donde se está desplegando porque alomejor no es la misma dirección)
