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
        st.write('Médico general CEUX ')
        st.write('Maestro en ciencias de la vida (MC)')
        st.caption('Centro de Investigación Científica y de Educación Superior de Ensenada (Centro CONACYT)')
        st.write('Cirujano general (Esp.Médica)') 
        st.caption('Centro Médico Nacional Siglo XXI/Universidad Nacional Autónoma de México')
        st.write('Editor principal')
        with st.container():
            st.caption('Dentro de mi experiencia cuento con una larga trayectoría en el ámbito clínico-hospitalario, tuve la oportunidad de trabajar en áreas de laboratorio clínico, consulta externa, urgencias y áreas hospitarias.')
            st.caption('Mi formación como maestro en ciencias me permitió conocer la investigación básica-experimental, realicé investigación en microbiología, biología celular y microscopía avanzada culminando con una tesis científica')
            st.caption('Durante mi formación como especialista en cirugía general tuve la oportunidad de estudiar a pacientes con alta mortalidad sometidos a colecistectomía, realizando tesis de posgrado y actualmente se encuentra en proceso de publicación.')
            
        
        

    with col2:
        Alonsimg='https://assets10.lottiefiles.com/packages/lf20_DZ8NLt7q12.json'
        lis=load_lottieurl(Alonsimg)
        st_lottie(lis,height=200,key=1234)  
    
    st.markdown('_________________')

            

