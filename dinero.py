from email.mime import image
from importlib.resources import path
import streamlit as st
from pathlib import Path
import requests
from streamlit_lottie import st_lottie
def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

def money():
    st.subheader('Pago')
    st.caption('Elige el servicio que necesitas para tu proyecto')
    st.write("")
    st.empty()
    st.write("")
    

    #generales
    st.info('Antes de realizar alguna transferencia, contactanos para tener seguimiento por parte de un editor')
    st.info('El editor resolvera vía email todas tus dudas y los pormenores de los servicios, tiempos de entrega, etc.')

    sol1,sol2=st.columns([2,1])
    with sol1:
        st.empty()
    with sol2:

        dinero=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_djwnoxew.json')
        st_lottie(dinero,height=150)
        
        
    colinit,colizq,colcentr,colder=st.columns(4)
    with colinit:
        st.markdown("[![Foo](Imagenes/Webapp medpost.png)](https://buy.stripe.com/14k2aQ9GJfDI8mYaEE)")
        st.caption('Protocolo de investigación nivel licenciatura')
    with colizq:
        #clickable image
        st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](https://buy.stripe.com/14k2aQ9GJfDI8mYaEE)")
        st.caption('Análisis estadístico')

    with colcentr:
        st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](https://buy.stripe.com/14k2aQ9GJfDI8mYaEE)")
        st.caption('Poster para congreso')


    with colder:
        st.markdown("[![Foo](/Users/alonso/Focus/Imagenes/Webapp medpost.png)](https://buy.stripe.com/14k2aQ9GJfDI8mYaEE)")
        st.caption('Poster para congreso')


