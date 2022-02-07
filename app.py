import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st





# Path del modelo preentrenado del proyecto Machine Learning.

MODEL_PATH = 'models/pickle_model.pkl'


# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):

    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


def main():
    st.image(
    "https://phantom-marca.unidadeditorial.es/772232b91f820ff4d5aaf3eae6dc4c31/resize/1320/f/jpg/assets/multimedia/imagenes/2020/10/15/16027188459256.jpg",
    width=None,) 

    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Título
    html_temp = """
    <h1 style="color:#2A759D;text-align:center;">¿Quien llega al TOP 1 del Premio Billboard Hot 100</h1>
    El Billboard Hot 100 es una gran lista de éxitos musicales de los 100 sencillos más vendidos en Estados Unidos, 
    que ayuda a promover la industria musical nacional e internacional, y se define como la más importante de las listas de
     Billboard junto con la Billboard 200.


    </div>
    
    """
   #181082 
 
    st.markdown(html_temp,unsafe_allow_html=True)

    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")
    E = st.text_input("Estado de Ánimo:")
    T = st.text_input("Tiempo:")
    G = st.text_input("Género:")
    Tipo = st.text_input("Tipo de Artista:")
    Edad = st.text_input("Edad:")
    Dura = st.text_input("Duración:")
    
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("EJECUTAR PARA PREDECIR :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.float_(E.title()),
                    np.float_(T.title()),
                    np.float_(G.title()),
                    np.float_(Tipo.title()),
                    np.float_(Edad.title()),
                    np.float_(Dura.title())]
        predictS = model_prediction(x_in, model)
        st.success('GANADOR DEL TOP : {}'.format(predictS[0]).upper())

if __name__ == '__main__':
    main()

    st.image(
    "https://tentulogo.com/wp-content/uploads/2018/05/billboard-logo-magazine.jpg",
    width=None) 

