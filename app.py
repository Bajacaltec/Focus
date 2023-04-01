       
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
from contacto import contacto
from dinero import money
from asesores import alonso, cesar, lissvia
from principal import displayPDF, principal
import numpy as np
import time
st.set_page_config(layout='wide',page_title='Tess extractor',menu_items=None,page_icon='Doit')


# encabezado y menú
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
tol1,tol2,tol3=st.columns(3)
with tol1:
    teesextractor=load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_yheqnvx7.json')
    st_lottie(teesextractor,height=100)
with tol2:
    st.write('')
    st.write('')
    st.caption('By Nunztec')
seleccion=option_menu(None,['Principal','Contacto','Editores','Pago'],orientation='horizontal',icons=['journal-medical','card-list','type'])



#Principal#
if seleccion=='Principal':
    principal()



#Editores

elif seleccion=='Editores':
    alonso()
    cesar()
    lissvia()       



#Contacto#
elif seleccion=='Contacto':
    contacto()

 
 
 
elif seleccion=='Pago':
    money()
    
#elif seleccion=='Ingresa':
 #   st.balloons()
    
  #  seleccion1=option_menu(None,['Portada','Índice','Just','Hipo','Plant','M-T','Resultados','Graficos','Figuras','Conclusiones','Discusión','Referencias'],orientation='horizontal',icons=['journal-medical','card-list','type'])
   # if seleccion1=='Portada':
        #Portada
    #    institucion,titulo,autores=st.columns([1,2,1])
     #   with institucion:
      #      id=st.number_input('ID')
       #     x=st.text_input('Institución:')
        #Menu#
        # modificación el menú#
        #iconos poner el nombre de bootstrap
        # with st.sidebar: (ponerlo en el sidebar)


        #como usar postgres
        #https://www.youtube.com/watch?v=M2NzvnfS-hI

        #Base render
        #conn = psycopg2.connect("dbname=base_vhom user=base_vhom_user password=8xUvM1YA3iw7Rjb1FxPTkgRf2xEFl87T host=dpg-cggclf02qv28tc396eng-a port=5432")
        #cur=conn.cursor()

        #creartabla='''CREATE TABLE IF NOT EXISTS prueba(id int PRIMARY KEY,
        #institucion varchar(40))'''
        #cur.execute(creartabla)
        #conn.commit()
        #cur.execute('''INSERT INTO prueba(id,institucion) VALUES(%s,%s);''',(id,x))

        #conn.commit()


        #cur.close()
        #conn.close()
                    
    # postgres://base_vhom_user:8xUvM1YA3iw7Rjb1FxPTkgRf2xEFl87T@dpg-cggclf02qv28tc396eng-a/base_vhom



    #deploy la app en Render
    #https://www.youtube.com/watch?v=4SO3CUWPYf0

    #subir app de streamlit en linea a Render
    #https://www.youtube.com/watch?v=4SO3CUWPYf0

    #hacer un cv en linea
    #https://www.youtube.com/watch?v=BXAeMICmUSQ


    #https://www.youtube.com/watch?v=3egaMfE9388

    #https://www.youtube.com/watch?v=VqgUkExPvLY

    #Navigation MEnu
    #https://youtu.be/hEPoto5xp3k

    # hacer uso de la autenticatión app de streamlit para controlar accesos
    # https://github.com/mkhorasani/Streamlit-Authenticator

    #Usar lottie para agregar animaciones en la pagina
    # https://github.com/andfanilo/streamlit-lottie
    #Baja Caltec o Nunztec
    #Nombre de la webapp



