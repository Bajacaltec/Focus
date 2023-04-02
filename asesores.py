import streamlit as st
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def alonso():
    st.title('Editores')
    col1,col2=st.columns([2,1])
    
    with col1:
        st.subheader('Dr. Fernando Alonso Núñez Moreno')
        st.write('Médico cirujano CEUX, Campus Tijuana')
        st.write('Maestro en ciencias de la vida (MC), CICESE')
        st.write('Cirujano general (Esp.Médica), Centro Médico Nacional Siglo XXI/UNAM')
        st.caption('Editor principal')
        

    with col2:
        Alonsimg='https://assets10.lottiefiles.com/packages/lf20_DZ8NLt7q12.json'
        lis=load_lottieurl(Alonsimg)
        st_lottie(lis,height=200,key=1234)  
    with st.expander('Mas información'):
        st.caption('El Dr. Núñez es un médico general, cirujano general e investigador con experiencia variada en las ciencias de la salud y biológicas, cuenta con trayectoría como docente en múltiples materias en la facultad de medicina de CEUX.')
        st.caption('A nivel maestria realizó sus estudios en el Centro de investigación de ciencias y estudios superiores de Ensenada, centro CONACYT de gran prestigio a nivel nacional, realizando estudios en microbiología, biología molecular y celular, así como microscopía avanzada. Cuenta con conocimientos de programación en lenguaje Python y lenguaje R para análisis estadísticos')
        st.caption('Durante su especialidad médica en el Centro Médico Nacional Siglo XXI IMSS en Ciudad de México realizó un estudio en pacientes con cardiopatia isquémica y colecistitis alitiásica, pendiente publicación')
        st.caption('Actualmente se encuentra en proceso de publicación de estudio sobre lesiones de vía biliar en pacientes sometidos a colecistectomía, publicación de reporte de caso de paciente con necrosis gástrica y en curso investigación sobre el uso de anestesia regiónal vs general en pacientes con apendicitis aguda sometidos a apendicectomía laparoscópica')
    st.markdown('_________________')

        
def cesar():
    col1,col2=st.columns([2,1])
    
    with col1:
        st.subheader('Dr. Cesar Octavio Núñez Moreno')
        st.write('Médico general UABC Cédula --, Campus Tijuana')
        st.write('Anestesiología (Esp.Médica), --')
        st.caption('Editor auxiliar ')
        st.markdown('_________________')

    with col2:
        cesarimg='https://assets10.lottiefiles.com/packages/lf20_DZ8NLt7q12.json'
        ces=load_lottieurl(cesarimg)
        st_lottie(ces,height=200)
        
        
def lissvia():
    col1,col2=st.columns([2,1])
    
    with col1:
        st.subheader('Dra. Lissvia Estéfani Acosta Gaxiola')
        st.write('Médico cirujano CEUX Cédula --, Campus Tijuana')
        st.caption('Editor auxiliar, traducción ')
        st.markdown('_________________')

    with col2:
        Lissimg='https://assets10.lottiefiles.com/packages/lf20_DZ8NLt7q12.json'
        lis=load_lottieurl(Lissimg)
        st_lottie(lis,height=200,key=2443)
        
        
            

