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
    
    x="""<head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" >
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"></script>
    <title>Button</title>
    <style>
        .container{
            height: 100px;
            width: 500px;
            margin-top: 60px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 style="text-align:center;"></h1>
        <a href="https://checkout.stripe.com/c/pay/cs_live_a15DxBP3qQObEUvZguNuMa6lpP18qvUoYQOKxe849qmAiwXWDQ0crJO7q9#fidkdWxOYHwnPyd1blppbHNgWjA0SHdfdDJDXH02VjJ8R11ESXdENDMzTk5hNX9oSUFHc2t1VGJBMkh%2FQ2ROUm8wcGJJSHFRcDJ2cTZof1ddQlFsVjdNfDR1M3Q0TTVhN0IwQXNrfEJ2UUZvNTVQcUF%2FVEhAUicpJ3VpbGtuQH11anZgYUxhJz8nNDFuN2RUPEJPY0FMPWhcZEBAJ3gl">
            <button class="btn btn-primary btn-lg">Comprar</button>
        </a>
    </div>
</body>
    

"""
    dinero=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_djwnoxew.json')
    st_lottie(dinero,height=150)
    st.caption('Antes de realizar alguna transferencia, contactanos para tener seguimiento por parte de un editor')

    

      
        
        
    colinit,colizq,colcentr,colder=st.columns(4)
    with colinit:
        st.image('Imagenes/Webapp medpost.png')
        st.markdown(x,unsafe_allow_html=True)

    with colizq:
        #clickable image
        st.image('Imagenes/Webapp medpost.png')

        st.markdown(x,unsafe_allow_html=True)


    with colcentr:
        st.image('Imagenes/Webapp medpost.png')

        st.markdown(x,unsafe_allow_html=True)


    with colder:
        st.image('Imagenes/Webapp medpost.png')

        st.markdown(x,unsafe_allow_html=True)
