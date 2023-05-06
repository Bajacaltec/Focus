from streamlit_lottie import st_lottie
import requests

import streamlit as st
@st.cache
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def contacto():
    col1,col2=st.columns(2)
    with col1:
        contact_form = """
        <form action="https://formsubmit.co/tessextractor@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        
        <input type="text" name="email" placeholder="Tu correo electrónico (email)" required>
        <input type="text" name="Número de telefono (opcional)" placeholder="Número de teléfono" >
        <input type="text" name="name" placeholder="¿Cual es tu nombre?" required>
        <textarea name="message" placeholder="¿En que podemos ayudarte?"></textarea>
        <input type="hidden" name="_next" value="https://correo-e5co.onrender.com">
        <button type="submit">Enviar</button>
        </form>
        """
        mail='Contactanos <i class="bi bi-mailbox"></i>'
        st.header('Contactanos :mailbox_closed:')
        st.caption('Ingresa tus datos para ponernos en contacto')
        st.markdown(contact_form, unsafe_allow_html=True)
            # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        local_css("style/style.css")
    with col2:
        pollo=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_se3w0ukg.json')
        st_lottie(pollo)

        