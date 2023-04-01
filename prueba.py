from pickle import TRUE
import streamlit as st

st.title('Bienvenidos a Tessextractor')

st.subheader('Nuestro equipo es un equipo multidisciplinario que se encargará de realizar un proyecto de investigación')
st.markdown('Nos enfocamos en tesis en ciencias de la salud y biológicas')

st.write('Utilizamos las sigueintes herramientas:')
st.info('Lenguaje de programación python')
st.info('Lenguaje R para el análisis estadístico')

x=st.number_input('Tu nos brindas los datos')
if x==1:
    st.balloons()

st.success('Nosotros hacemos tu proyecto de investigación y el análisis estadístico')
