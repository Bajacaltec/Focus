       
import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
from dinero import money
from asesores import alonso, cesar, lissvia
import numpy as np
import time
import base64

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def main():
    fol1,fol2=st.columns([5,1])
    with fol1:
        st.subheader('Trabajos recientes')
    with fol2:
        mex=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_jidselhy.json')
        st_lottie(mex,height=50)
    eins,swei,drei,fear,funf,sechts=st.columns(6)
    with eins:
        st.image('Imagenes/articulocureus.png')
        st.caption('Reporte de caso (inglés); A Case of Gastric Necrosis Due To Small Bowel Obstruction Caused By a Strangulated Femoral Hernia: Case report')
    with swei:
        st.image('Imagenes/posterneurospora.png')
        st.caption('Poster para congreso nacional en ciencias biológicas: Functional Analysis of a Class II Myosina in the Apical Organization of the Filamentous Fungi Neurospora crassa')
    with drei:
        st.image('Imagenes/tesiscxcolcardio.png')
        st.caption('Tesis de especialidad médica: Morbilidad y mortalidad en pacientes con enfermedades cardiovasculares sometidos a colecistectomía por colecistitis aguda en el Centro Médico Nacional Siglo XXI')
    with fear:
        st.image('Imagenes/tesismaestria.png')
        st.caption('Tesis para obtener el grado de maestro en ciencias: Análisis funcional de la miosina de clase II en la organización apical en el hongo filamentoso Neurospora crassa')

    with funf:
        st.image('Imagenes/Encina.png')
        st.caption('Colaboración en curso publicación artículo en ingles de tesis de especialidad médicas:Factores asociados a estenosis de hepaticoyeyunoanastomosis en pacientes con disrupción de vía biliar')
    with sechts:
        st.image('Imagenes/Gonzalez.png')
        st.caption('Tesis de especialidad médicas: Experiencia del manejo quirúrgico de la pancreatitis crónica en el hospital de especialidades "Dr. Bernardo Sepulveda" Centro Médico Nacional Siglo XXI')
        
    
    st.markdown('_____________')
    
    uno,dos,tres=st.columns([1,1,1])
    
    with uno:
        st.latex(r'''s = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2} 
            ''')   
         
        lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_iYvSqSMKZB.json")
        st_lottie(lottie_hello,height=70)  
        
        st.caption('Olvidate de fórmulas complicadas, la correcta aplicación de análisis estadísticos y dejanos a ayudarte a terminar tu proyecto en el menor tiempo posible y con la mejor calidad')

        st.markdown('____________')
        st.caption('Análisis estadístico y desarrollo de plataforma de captura a la medida, utilizamos los siguientes lenguajes de programación')
        """### gif from local file"""
        #file_ = open("https://github.com/Bajacaltec/Focus/blob/main/Imagenes/gife.gif", "rb")
        #contents = file_.read()
        #data_url = base64.b64encode(contents).decode("utf-8")
        #file_.close()

        #st.markdown(
         #   f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width="310" height="200">',
          #  unsafe_allow_html=True,
        #)        

        # gif
        st.write("")
        st.info('Lenguaje de programación python')
        st.info('Lenguaje de programación R')
        
        
           
    with dos:
        st.subheader('¿No sabes por donde empezar?')
        with st.expander('Marco teórico',expanded=True):
            st.success('Con nuestra guía terminarás tu proyecto en el menor tiempo posible, con el menor dolor de cabeza posible, y con la mejor calidad posible.')
            st.warning('Realiza tu protocolo de investigación con un asesor directamente trabajando contigo lado a lado.')
        with st.expander('Que ofrece Tessextractor',expanded=True):
            st.warning('Diseño metodológico adecuado, los errores de ejecución se eliminan o disminuyen con un buen diseño metodológico.')
            st.warning('Análisis estadístico preciso y adecuado con el lenguaje R.')
        st.warning('Apoyo en la redacción y traducción de tesis para publicación')
       
    with tres:
        
        st.write('¿Qué es la investigación, sino una cita a ciegas con el conocimiento? ')
        st.latex('Will Harvey')
        lotbook=load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_tnrzlN.json')
        st_lottie(lotbook,width=80)
        
        st.subheader('Desarrollo de Webapps para facilitar tu trabajo')
        st.caption('Pruebalas')
        st.image('https://github.com/Bajacaltec/Focus/blob/main/Imagenes/Webapp%20medpost.png')    
        st.video('/Users/alonso/Focus/Imagenes/cxcorazon.mp4',start_time=0)
        st.caption('Video 1. Toracotomia anterolateral izquierda con pericardiotomía y exposición de miocardio. Cirugía por trauma penetrante de tórax por proyectil de arma de fuego en hospital de traumatología Lomas Verdes IMSS')


    
