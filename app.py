       
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
import principal
st.set_page_config(layout='wide',page_title='Tess extractor',menu_items=None,page_icon='Doit')

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