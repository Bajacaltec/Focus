from email.mime import image
from importlib.resources import path
import streamlit as st
from pathlib import Path


def money():
    st.title('Elige el servicio que necesitas')
   
    #generales
    strype_salida= "https://buy.stripe.com/14k2aQ9GJfDI8mYaEE"
    email="mdfnunez@gmail.com"
    
    colinit,colizq,colcentr,colder=st.columns(4)
    with colinit:
        st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](https://buy.stripe.com/14k2aQ9GJfDI8mYaEE)")
        st.caption('Protocolo de investigación nivel licenciatura')
    with colizq:
        #clickable image
        st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](https://buy.stripe.com/14k2aQ9GJfDI8mYaEE)")
        st.caption('Análisis estadístico')

    with colcentr:
        st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](https://buy.stripe.com/14k2aQ9GJfDI8mYaEE)")
        st.caption('Poster para congreso')


    with colder:
        st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](https://buy.stripe.com/14k2aQ9GJfDI8mYaEE)")

