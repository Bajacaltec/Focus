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
            
            
            
            
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from matplotlib.pyplot import title
import streamlit as st
import psycopg2
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide',page_title='Haz tu tesis')

seleccion=option_menu(None,['Portada','Índice','Just','Hipo','Plant','M-T'],orientation='horizontal',icons=['journal-medical','card-list','type'])
#Portada
institucion,titulo,autores=st.columns([1,2,1])
with institucion:
    id=st.number_input('ID')
    x=st.text_input('Institución:')
#Menu#
# modificación el menú#
#iconos poner el nombre de bootstrap
# with st.sidebar: (ponerlo en el sidebar)


#como usar postgres
#https://www.youtube.com/watch?v=M2NzvnfS-hI

#Base render
conn = psycopg2.connect("dbname=base_vhom user=base_vhom_user password=8xUvM1YA3iw7Rjb1FxPTkgRf2xEFl87T host=dpg-cggclf02qv28tc396eng-a port=5432")
cur=conn.cursor()

creartabla='''CREATE TABLE IF NOT EXISTS prueba(id int PRIMARY KEY,
institucion varchar(40))'''
cur.execute(creartabla)
conn.commit()
cur.execute('''INSERT INTO prueba(id,institucion) VALUES(%s,%s);''',(id,x))

conn.commit()


cur.close()
conn.close()

