       
from re import S
from turtle import width
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

   
        
    
    hol1,hol2,hol3=st.columns(3)
    with hol1:
        busqueda=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json')
        st_lottie(busqueda,height=100)
        st.subheader('Análisis estadístico')
        
    with hol2:
        tesis=load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_y2ryub2r.json")
        st_lottie(tesis,height=100)
        st.subheader('Tesis de investigación')
       
    with hol3:
        publicacion=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_kcxosgub.json')
        st_lottie(publicacion,height=100)
        st.subheader('Publicación de artículo')
    st.caption('Podemos ayudarte en muchas otras etapas de tu proyecto, desde busqueda de información, formato de referencias, presentación para defensa de tésis, revisión de texto y correción ortográfica, contáctanos para recibir información específica sobre el costo de la asesoría dependiendo de tus necesidades')
    st.markdown("______________")
    
    
    st.subheader('Trabajos recientes')
        #Trabajos recientes
    eins,swei,drei,fear,funf,sechts=st.columns(6)
    with eins:
        st.image('Imagenes/articulocureus.png')
        st.caption('Reporte de caso (En proceso de publicación); A Case of Gastric Necrosis Due To Small Bowel Obstruction Caused By a Strangulated Femoral Hernia: Case report')
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

    
    #columna 1
    
    with uno:
        st.latex(r'''s = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2} 
            ''')   
         
        lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_iYvSqSMKZB.json")
        st_lottie(lottie_hello,height=70)  
        
        st.caption('Olvidate de fórmulas complicadas, la correcta aplicación de análisis estadísticos y dejanos a ayudarte a terminar tu proyecto en el menor tiempo posible y con la mejor calidad')

        st.markdown('____________')
        st.caption('Análisis estadístico y desarrollo de plataforma de captura personalizado, utilizamos los siguientes lenguajes de programación')
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
        
        
    #Columna 2    
    with dos:
        st.subheader('¿No sabes por donde empezar?')
        st.markdown("- Encuentra el tema que te interesa (área de especialidad, patología, algún caso en particular")
        st.markdown("- Busqueda de información(Artículos, libros, experiencias")
        st.markdown("- Hazte una pregunta de investigación: ¿El uso de metformina vs insulina aumenta la posibilidad de hipoglicemias en un paciente con Diabetes mellitus tipo II? 🤔 ")
        st.markdown("- Y así nace un proyecto de investigación")

        st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
        ''', unsafe_allow_html=True)
        st.markdown('___________')       
        st.info('Contactanos para poder ayudarte con tu proyecto de investigación')
    with tres:
        
        st.write('¿Qué es la investigación, sino una cita a ciegas con el conocimiento? ')
        st.latex('Will Harvey')
        lotbook=load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_tnrzlN.json')
        st_lottie(lotbook,width=80)
        
        st.subheader('Desarrollo de Webapps para facilitar tu trabajo')
        st.image('Imagenes/Webapp medpost.png')   
        st.caption('Proximamente') 
    
    st.markdown('_________')
    st.subheader('Media')
    kol1,kol2,kol3=st.columns([1,1,2])
    with kol1:
        st.video('Imagenes/cxcorazon.mp4',)
        st.info('Video 1. Toracotomia anterolateral izquierda con pericardiotomía y exposición de miocardio. Cirugía por trauma penetrante de tórax por proyectil de arma de fuego en hospital de traumatología Lomas Verdes IMSS')

    with kol2:
        st.empty()
    st.markdown('____________')
    st.caption('Tessextractor fue elaborado por Nunztec con python y streamlit, para mayor información sobre nuestros productos, ingresa a la página de contacto y envianos un E mail')
 
 