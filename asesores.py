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
        
        

    with col2:
        Alonsimg='https://assets10.lottiefiles.com/packages/lf20_DZ8NLt7q12.json'
        lis=load_lottieurl(Alonsimg)
        st_lottie(lis,height=200,key=1234)  
    
    st.markdown('_________________')

            

