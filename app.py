from boto import config
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from matplotlib.pyplot import title
import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide',page_title='Haz tu tesis')
# revisar este como nicial
#Menu#
# modificación del menú#
#iconos poner el nombre de bootstrap
# with st.sidebar: (ponerlo en el sidebar)

cur=sqlite3.connect('Db.db')
con=cur.cursor()
con.execute('''CREATE TABLE IF NOT EXISTS proteus (Folio INTEGER PRIMARY KEY,
            Institucion TEXT)''')
cur.commit()


seleccion=option_menu(None,['Portada','Índice','Just','Hipo','Plant','M-T'],orientation='horizontal',icons=['journal-medical','card-list','type'])

#Portada
if seleccion=='Portada':
        st.write('Menú')
        institucion,titulo,autores=st.columns([1,2,1])
        with institucion:
            x=st.text_input('Institución:')
            con.execute('INSERT INTO proteus VALUES(1,"hola")')
            cur.commit()
        with titulo:
            st.text_area('Título:')

        with autores:
            st.text_input('Autor 1:')
            st.text_input('Autor 2:')
            st.text_input('Autor 3:')
            
            




#deploy la app en Render
#https://www.youtube.com/watch?v=4SO3CUWPYf0

#subir app de streamlit en linea a Render
#https://www.youtube.com/watch?v=4SO3CUWPYf0

#hacer un cv en linea
#https://www.youtube.com/watch?v=BXAeMICmUSQ


#https://www.youtube.com/watch?v=3egaMfE9388

#https://www.youtube.com/watch?v=VqgUkExPvLY

#Navigation MEnu
#https://youtu.be/hEPoto5xp3k

# hacer uso de la autenticatión app de streamlit para controlar accesos
# https://github.com/mkhorasani/Streamlit-Authenticator

#Usar lottie para agregar animaciones en la pagina
# https://github.com/andfanilo/streamlit-lottie
#Baja Caltec o Nunztec
#Nombre de la webapp



