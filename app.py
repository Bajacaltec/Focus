import streamlit as st


# hacer uso de la autenticatión app de streamlit para controlar accesos
# https://github.com/mkhorasani/Streamlit-Authenticator

#Usar lottie para agregar animaciones en la pagina
# https://github.com/andfanilo/streamlit-lottie
#Baja Caltec o Nunztec
#Nombre de la webapp

menu=st.selectbox('Menú',['Portada','Índice'])

st.text_input('Ponle')