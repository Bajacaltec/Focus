       
from re import S
from turtle import width
import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
from dinero import money
from asesores import alonso
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
    st.image('Imagenes/análisis estadístico.001.jpeg')   
       
    hol1,hol2,hol3=st.columns(3)
    with hol1:
        busqueda=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json')
        st_lottie(busqueda,height=100)
        st.subheader('Análisis estadístico')
        st.caption('Análisis de base de datos con R')
        
    with hol2:
        tesis=load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_y2ryub2r.json")
        st_lottie(tesis,height=100)
        st.subheader('Tesis de investigación')
        st.caption('Tesis a nivel licenciatura y posgrado')
       
    with hol3:
        publicacion=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_kcxosgub.json')
        st_lottie(publicacion,height=100)
        st.subheader('Publicación de artículo')
        st.caption('Artículos en español e inglés')
    st.markdown("______________")
    
    
    st.subheader('Trabajos recientes')
        #Trabajos recientes
    eins,swei,drei,fear=st.columns(4)
    with eins:
        st.image('Imagenes/articulocureus.png')
        st.caption('https://www.cureus.com/articles/147372-gastric-necrosis-due-to-small-bowel-obstruction-a-case-report')
    with swei:
        st.image('Imagenes/posterneurospora.png')
    with drei:
        st.image('Imagenes/tesiscxcolcardio.png')
    with fear:
        st.image('Imagenes/tesismaestria.png')
        st.caption('https://cicese.repositorioinstitucional.mx/jspui/handle/1007/662')

   
    
    st.markdown('_____________')
    
    
    
    uno,dos,tres=st.columns([1,1,1])

    
    #columna 1
    
    with uno:
        st.latex(r'''s = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2} 
            ''')   
         
        lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_iYvSqSMKZB.json")
        st_lottie(lottie_hello,height=70)  
        
        st.caption('Olvidate de fórmulas y técnicas estadísticas complicadas')
        st.markdown('____________')
        st.caption('Análisis estadístico y programacíon de plataforma de captura personalizado')
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
        st.caption('Utilizamos los siguientes lenguajes de programación')

        st.write("")
        st.info('Lenguaje de programación python')
        st.info('Lenguaje de programación R')
        
        
    #Columna 2    
    with dos:
        st.subheader('¿No sabes por donde empezar?')
        st.markdown("Encuentra el tema que te interesa")
        st.markdown("Busca información(Artículos, libros, etc.)")
        st.markdown("Haz una pregunta de investigación: ¿El uso de metformina vs insulina aumenta la posibilidad de hipoglicemias en un paciente con Diabetes mellitus tipo II? 🤔 ")
        st.markdown("Y así nace un proyecto de investigación")

        st.markdown('''
        <style>
        [data-testid="stMarkdownContainer"] ul{
            padding-left:40px;
        }
        </style>
        ''', unsafe_allow_html=True)
        st.markdown('___________')       
        st.info('Contactanos para poder ayudarte con tu proyecto de investigación')
        st.video('Imagenes/recortado R.mov')
        st.info('Análisis con R')
    with tres:
        
        st.write('¿Qué es la investigación, sino una cita a ciegas con el conocimiento? ')
        st.latex('Will Harvey')
        lotbook=load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_tnrzlN.json')
        st_lottie(lotbook,width=80)
        
        st.subheader('Web app Tessextractor con IA')
        st.caption('Se encuentra en desarrollo la Webapp de Tessextractor que con el apoyo de la inteligencia artificial faicilitará el desarrollo de trabajos de investigación, esperala proximamente')
        workinprog=load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_vDd5lrv57P.json')
        st_lottie(workinprog,width=300)
    
    kol1,kol2,kol3=st.columns([1,1,2])
    with kol1:
        st.empty()
       
        
    with kol2:
        st.empty()
 
 