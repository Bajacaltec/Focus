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
    # boton de pago

    gol1,gol2=st.columns([5,2])
    with gol1:
        st.subheader('Área de pago')
        st.caption('Se aceptan todas las tarjetas American express, Visa o Mastercard, depósito en OXXO y apple Pay')
    with gol2:
        dinero=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_djwnoxew.json')
        st_lottie(dinero,height=150)
    st.markdown('__________')
    
    
    #tesis de investigación nivel posgrado
    bol1,bol2,bol3=st.columns([3,1,1])
    with bol1:
        st.caption('Servicio')
        st.subheader('Tesis de investigación nivel posgrado con captura de datos')
        st.caption('Elaboración de Tesis a nivel posgrado con captura de datos')


    b="""<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>Button</title>
    <style>
        .container{
            height: 50px;
            width: 100px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1    "text-align:center;"></h1>
        <a href="https://buy.stripe.com/5kA7vaf132QWbza14e">
            <button class="btn btn-primary btn-lg">Pagar</button>
        </a>
    </div>
</body>
    

"""

    with bol2:
        st.image('Imagenes/captura.jpg')
        st.info(' MXN 5,500.00')

    with bol3:
        st.markdown(b,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('________')
    
    
    #Boton de pago
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
        <a href="https://buy.stripe.com/dR6bLqf1363832EcN2">
            <button class="btn btn-primary btn-lg">Pagar</button>
        </a>
    </div>
</body>
    

"""


    #Análisis de datos
    lol1,lol2,lol3=st.columns([3,1,1])
    
    with lol1:
        st.caption('Servicio')
        st.subheader('Análisis estadístico')
        st.caption('Análisis con R, se debe proporcionar base de datos')

    with lol2:
        st.image('Imagenes/anestadistica.jpg')
        st.info(' MXN 1900.00')


    with lol3:
        st.markdown(x,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('_________')
    
    
    
    
    #Procotolo de investigación nivel licenciatura
    lol1,lol2,lol3=st.columns([3,1,1])
#PRUEBA
    with lol1:
        st.caption('Servicio')
        st.subheader('Protocolo de investigación nivel licenciatura')
        st.caption('Elaboración de protocolo de investigación a nivel licenciatura')


    L="""<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>Button</title>
    <style>
        .container{
            height: 50px;
            width: 100px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1    "text-align:center;"></h1>
        <a href="https://buy.stripe.com/7sI8ze6ux8bgav614l">
            <button class="btn btn-primary btn-lg">Pagar</button>
        </a>
    </div>
</body>
    

"""

    with lol2:
        st.image('Imagenes/protolic.jpeg')
        st.info(' MXN 1700.00')

    with lol3:
        st.markdown(L,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('_________')

    
    
    
    
    
    
    #Tesis de licenciatura
    
    rol1,rol2,rol3=st.columns([3,1,1])
    
    with rol1:
        st.caption('Servicio')
        st.subheader('Tesis de licenciatura')
        st.caption('Elaboración de tesis de nivel licenciatura')



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
        <a href="https://buy.stripe.com/7sI6r6f13dvAfPq8wO">
            <button class="btn btn-primary btn-lg">Pagar</button>
        </a>
    </div>
</body>
    

"""

    with rol2:
        st.image('Imagenes/tesis.tiff')
        st.info(' MXN 2900.00')

    with rol3:
        st.markdown(Y,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('_________')

    zol1,zol2,zol3=st.columns([3,1,1])
    with zol1:
        st.caption('Servicio')
        st.subheader('Protocolo de investigación nivel posgrado')
        st.caption('Elaboración de protocolo de investigación a nivel posgrado')



    #Protocolo de investigación nivel posgrado
    W="""<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>Button</title>
    <style>
        .container{
            height: 50px;
            width: 100px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1    "text-align:center;"></h1>
        <a href="https://buy.stripe.com/00g5n2cSV77c9r29AO">
            <button class="btn btn-primary btn-lg">Pagar</button>
        </a>
    </div>
</body>
    

"""

    with zol2:
        st.image('Imagenes/proto_posgrado.jpg')
        st.info(' MXN 2800.00')

    with zol3:
        st.markdown(W,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('_________')



    #tesis de investigación nivel posgrado
    pol1,pol2,pol3=st.columns([3,1,1])
    with pol1:
        st.caption('Servicio')
        st.subheader('Tesis de investigación nivel posgrado')
        st.caption('Elaboración de Tesis a nivel posgrado')


    p="""<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>Button</title>
    <style>
        .container{
            height: 50px;
            width: 100px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1    "text-align:center;"></h1>
        <a href="https://buy.stripe.com/cN202I069ajoeLm7sH">
            <button class="btn btn-primary btn-lg">Pagar</button>
        </a>
    </div>
</body>
    

"""

    with pol2:
        st.image('Imagenes/posgradotesis.png')
        st.info(' MXN 3900.00')

    with pol3:
        st.markdown(p,unsafe_allow_html=True)
        st.subheader("")
    st.markdown('_________')
        

    
    
    
    

    

      
       