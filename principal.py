       
from operator import truediv
from turtle import width
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from matplotlib.pyplot import title
import streamlit as st
import requests
import matplotlib.pyplot as plt
import json
from streamlit_lottie import st_lottie
import psycopg2
from streamlit_option_menu import option_menu
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

def principal():
    uno,dos,tres=st.columns([2,1,1])
    with uno:
        with st.expander('Análisis estadístico',expanded=True):
            st.info('Olvidate de fórmulas complicadas, la correcta aplicación de análisis estadísticos y dejanos a ayudarte a terminar tu proyecto en el menor tiempo posible y con la mejor calidad')
            st.latex(r'''s = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2} 
                ''')    
        lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_iYvSqSMKZB.json")
        st_lottie(lottie_hello,height=150)  
        st.image('/Users/alonso/Focus/Imagenes/posterneurospora.png')
        st.info('Poster para congreso de ciencias biológicas')
        st.image('/Users/alonso/Focus/Imagenes/articulocureus.png')
        st.success('Reporte de caso de necrosis gástrica publicado en revista Cureus en idioma inglés')
        st.info('Gráfica tus datos para hacer mas entendibles tus datos ')
           
    with dos:
        st.subheader('¿No sabes por donde empezar?')
        with st.expander('Marco teórico',expanded=True):
            st.success('Con nuestra guía terminarás tu proyecto en el menor tiempo posible, con el menor dolor de cabeza posible, y con la mejor calidad posible.')
            st.warning('Realiza tu protocolo de investigación con un asesor directamente trabajando contigo lado a lado.')
        with st.expander('Que ofrece Tessextractor',expanded=True):
            st.warning('Diseño metodológico adecuado, los errores de ejecución se eliminan o disminuyen con un buen diseño metodológico.')
            st.warning('Análisis estadístico preciso y adecuado con el lenguaje R.')
        st.warning('Apoyo en la redacción y traducción de tesis para publicación')
        st.video('/Users/alonso/Focus/Imagenes/cxcorazon.mp4',start_time=0)
        st.error('Video 1. Toracotomia anterolateral izquierda con pericardiotomía y exposición de miocardio. Cirugía por trauma penetrante de tórax por proyectil de arma de fuego en hospital de traumatología Lomas Verdes IMSS')
       
    with tres:
        mex=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_jidselhy.json')
        st_lottie(mex,height=50)
        st.write('¿Qué es la investigación, sino una cita a ciegas con el conocimiento? ')
        st.latex('Will Harvey')
        lotbook=load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_tnrzlN.json')
        st_lottie(lotbook)
        st.info('Realiza tu proyecto de investigación en la modalidad y alcance que requieras en tiempo record')
        st.image('/Users/alonso/Focus/Imagenes/tesiscxcolcardio.png')
        st.success('Utilizamos el lenguaje R para el análisis estadístico y programación con python para hacer mas fácil tu proceso de desarrollo de tu proyecto de investigación, no necesitas nada mas que nuestra orientación y herramientas')
        st.image('/Users/alonso/Focus/Imagenes/logo.jpeg')
        st.subheader('Visita el Medpost un diario de salud con las noticias más actuales')
        st.markdown('https://elmedpost.wordpress.com')
        st.image('/Users/alonso/Focus/Imagenes/Webapp medpost.png')
        st.subheader('Utiliza nuestras Webapps')
        displayPDF('/Users/alonso/Focus/Tesis myo2.pdf')
        
def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="200" height="280" type="application/pdf"></iframe>'    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)
        
