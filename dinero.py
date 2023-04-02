from email.mime import image
from importlib.resources import path
from tkinter import Y
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
    x="""<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>Button</title>
    <style>
        .container{
            height: 50px;
            width: 100px;
            margin-top: 20px;
            style= background-color:#2BE039
        }
    </style>
</head>
<body>
    <div class="container">
        <h1    "text-align:center;"></h1>
        <a href="https://buy.stripe.com/fZeaHm9GJfDIeLmbIJ">
            <button class="btn btn-primary btn-lg">Comprar</button>
        </a>
    </div>
</body>
    

"""


    gol1,gol2=st.columns([5,2])
    with gol1:
        st.subheader('Área de pago')
        st.caption('Se aceptan todas las tarjetas American express, Visa o Mastercard, depósito en OXXO y apple Pay')
        st.write('Antes de realizar alguna transferencia, contactanos para tener seguimiento por parte de un editor')
    with gol2:
        dinero=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_djwnoxew.json')
        st_lottie(dinero,height=150)
    st.markdown('__________')

    #Análisis de datos
    lol2,lol3,lol4=st.columns([3,1,1])
    
    with lol2:
        st.caption('Producto')
        st.subheader('Análisis estadístico')
        st.caption('Análisis con R, se debe proporcionar base de datos')

    with lol3:
        st.image('Imagenes/anestadistica.jpg')

    with lol4:
        st.markdown(x,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('_________')
    #
    
    #Tesis de licenciatura
    rol1,rol2,rol3=st.columns([3,1,1])
    
    with rol1:
        st.caption('Producto')
        st.subheader('Tesis de licenciatura')
        st.caption('Elaboración de tesis de nivel licenciatura, cuartillas máximo 40 cuartillas')



    #ENLACE PARA STRIPE EN HTML
    Y="""<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>Button</title>
    <style>
        .container{
            height: 50px;
            width: 100px;
            margin-top: 20px;
            style= background-color:#2BE039
        }
    </style>
</head>
<body>
    <div class="container">
        <h1    "text-align:center;"></h1>
        <a href="https://buy.stripe.com/eVabLqdWZ77c46I146">
            <button class="btn btn-primary btn-lg">Comprar</button>
        </a>
    </div>
</body>
    

"""

    with rol2:
        st.image('Imagenes/tesis.tiff')
    with rol3:
        st.markdown(Y,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('_________')

    zol1,zol2,zol3=st.columns([3,1,1])
#PRUEBA
    with zol1:
        st.caption('Producto')
        st.subheader('Protocolo de investigación nivel posgrado')
        st.caption('Elaboración de tesis de nivel licenciatura, cuartillas máximo 40 cuartillas')



    #ENLACE PARA STRIPE EN HTML
    W="""<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>Button</title>
    <style>
        .container{
            height: 50px;
            width: 100px;
            margin-top: 20px;
            style= background-color:#2BE039
        }
    </style>
</head>
<body>
    <div class="container">
        <h1    "text-align:center;"></h1>
        <a href="https://buy.stripe.com/14kg1GdWZajo7iUfZ2">
            <button class="btn btn-primary btn-lg">Comprar</button>
        </a>
    </div>
</body>
    

"""

    with zol2:
        st.image('Imagenes/proto_posgrado.jpg')
    with zol3:
        st.markdown(W,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('_________')

        


    
    
    
    

    

      
       