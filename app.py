import streamlit as st
from annotated_text import annotated_text
import streamlit_authenticator as stauth


# hacer uso de la autenticatión app de streamlit para controlar accesos
# https://github.com/mkhorasani/Streamlit-Authenticator

#Usar lottie para agregar animaciones en la pagina
# https://github.com/andfanilo/streamlit-lottie
#Baja Caltec o Nunztec
#Nombre de la webapp

menu=st.selectbox('Menú',['Portada','Índice'])
annotated_text(
    "This ",
    ("Bolitochs", "verb"),
    " some ",
    ("annotated", "adj"),
    ("text", "noun"),
    " for those of ",
    ("you", "pronoun"),
    " who ",
    ("like", "verb"),
    " this sort of ",
    ("thing", "noun"),
    "."
)
st.text_input('Ponle')