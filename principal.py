       
from re import S
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
    st.subheader('Nos especializamos en proyectos de investigación en el área de la salud. ')

    fol1,fol2,fol3=st.columns([5,1,1])
    with fol1:
        st.write('Podemos ayudarte en diferentes etapas de tu proyecto')
    
    with fol2:
        st.empty()
    with fol3:
        st.empty()
        
    
    hol1,hol2,hol3=st.columns(3)
    with hol1:
        st.info('Redacción de protocolo de investigación y búsqueda de información')
        busqueda=load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_5KobUw.json')
        st_lottie(busqueda,height=100)
        st.info('Análisis estadístico')
    with hol2:
        st.info('Escritura de tésis')
        tesis=load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_y2ryub2r.json")
        st_lottie(tesis,height=120)
        st.info('Guia para la escritura de tesis')
    with hol3:
        st.info('Publicación de artículo en idioma español o inglés')
    
    st.markdown("______________")
    
    
    st.subheader('Trabajos recientes')
        #Trabajos recientes
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
        st.caption('Colaboración en curso publicación de tesis de especialidad médicas:Factores asociados a estenosis de hepaticoyeyunoanastomosis en pacientes con disrupción de vía biliar')
    with sechts:
        st.image('Imagenes/Gonzalez.png')
        st.caption('Colaboración en curso para la publicación de tesis de especialidad médicas: Experiencia del manejo quirúrgico de la pancreatitis crónica en el hospital de especialidades "Dr. Bernardo Sepulveda" Centro Médico Nacional Siglo XXI')
        
    
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
        file_ = open("Imagenes/gife.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="cat gif" width="310" height="200">',
            unsafe_allow_html=True,
        )        

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
        st.image('Imagenes/Webapp medpost.png')    
        st.video('Imagenes/cxcorazon.mp4',start_time=0)
        st.caption('Video 1. Toracotomia anterolateral izquierda con pericardiotomía y exposición de miocardio. Cirugía por trauma penetrante de tórax por proyectil de arma de fuego en hospital de traumatología Lomas Verdes IMSS')

 
 