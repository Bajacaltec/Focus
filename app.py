import streamlit as st
from annotated_text import annotated_text
import streamlit_authenticator as stauth

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