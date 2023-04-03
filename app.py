       
import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from contacto import contacto
from dinero import money
from asesores import alonso, cesar, lissvia
import numpy as np
import time
from principal import main
import base64
st.set_page_config(layout='wide',page_title='Tess extractor',menu_items=None,page_icon='Tessextractor', )

####
# encabezado y menú
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
tol1,tol2,tol3=st.columns([1,2,1])
with tol1:
    teesextractor=load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_yheqnvx7.json')
    st_lottie(teesextractor,height=100)
with tol2:
    st.write('')
    st.write('')
    st.caption('By Nunztec')
with tol3:
    mex=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_jidselhy.json')
    st_lottie(mex,height=50)
    
    
seleccion=option_menu(None,['Principal','Contacto','Editores','Pago'],orientation='horizontal',icons=['journal-medical','card-list','type'], styles={
        "container": {"padding": "0!important", "background-color": "#E5EFF6"},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"font-size": "18px", "text-align": "Center", "margin":"0px", "--hover-color": "#D3EA8B"},
        "nav-link-selected": {"background-color": "#407BD2"},
    })

#Principal#
if seleccion=='Principal':
    main()



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


st.markdown('________')
st.subheader('Contacto')
col1,col2,colx=st.columns([3,1,1])
with col1:
    st.caption('Correo electrónico: elmedpost@gmail.com o mdfnunez@gmail.com')
    st.caption('Pagina de Facebook:')
    st.image('Imagenes/whatsapp.png')
    st.caption('Telefono Wha: +529617024389')


with col2:
    hu=load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_twijbubv.json')
    st_lottie(hu,height=150)
st.markdown('_________')
st.caption('Tessextractor fue elaborado por Nunztec con el lenguaje de programación python y streamlit, para mayor información sobre nuestros productos, ingresa a la página de contacto y envianos un E mail')
