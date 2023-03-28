from matplotlib.ft2font import HORIZONTAL, VERTICAL
from matplotlib.pyplot import title
import streamlit as st
import psycopg2
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide',page_title='Haz tu tesis')

seleccion=option_menu(None,['Portada','Índice','Just','Hipo','Plant','M-T'],orientation='horizontal',icons=['journal-medical','card-list','type'])
#Portada
if seleccion=='Portada':
    st.write('Menú')
    institucion,titulo,autores=st.columns([1,2,1])
    with institucion:
        id=st.number_input('id)')
        x=st.text_input('Institución:')
#Menu#
# modificación el menú#
#iconos poner el nombre de bootstrap
# with st.sidebar: (ponerlo en el sidebar)


#como usar postgres
#https://www.youtube.com/watch?v=M2NzvnfS-hI

st.write('Prueba de upload')
#Base render
conn = psycopg2.connect("dbname=base_vhom user=base_vhom_user password=8xUvM1YA3iw7Rjb1FxPTkgRf2xEFl87T host=dpg-cggclf02qv28tc396eng-a port=5432")
cur=conn.cursor()

creartabla='''CREATE TABLE IF NOT EXISTS prueba(id int PRIMARY KEY,
institucion varchar(40))'''
cur.execute(creartabla)
cur.execute('''INSERT INTO prueba(institucion) VALUES('e');''')

conn.commit()


cur.close()
conn.close()

seleccion=option_menu(None,['Portada','Índice','Just','Hipo','Plant','M-T'],orientation='horizontal',icons=['journal-medical','card-list','type'])
#Portada
if seleccion=='Portada':
        st.write('Menú')
        institucion,titulo,autores=st.columns([1,2,1])
        with institucion:
            x=st.text_input('Institución:')
            
            
# postgres://base_vhom_user:8xUvM1YA3iw7Rjb1FxPTkgRf2xEFl87T@dpg-cggclf02qv28tc396eng-a/base_vhom



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



