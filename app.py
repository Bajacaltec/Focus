       
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from matplotlib.pyplot import title
import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import psycopg2
from streamlit_option_menu import option_menu

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(layout='wide',page_title='Haz tu tesis')

eins,swei,drei=st.columns([1,2,1])
with eins:
    st.write('lotbctec')
with drei:
    mex=load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_jidselhy.json')
    st_lottie(mex,height=50)
seleccion=option_menu(None,['Principal','Asesores','Trabajos publicados','Contacto','Ingresa'],orientation='horizontal',icons=['journal-medical','card-list','type'])

if seleccion=='Principal':
    uno,dos,tres=st.columns([1,2,1])
    with uno:
        lotbook=load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_tnrzlN.json')
        st_lottie(lotbook)
        st.info('En Tesisya nos encargamos de guiarte con nuestra Webapp, personalizada para el trabajo de investigación en cuestión te apoyamos desde el inicio en cuanto a la elección de tema de investigación, búsqueda de información, desarrollo del proyecto, análisis estadístico CORRECTO, escritura de la tesis, publicación y traducción al ingles')
        
    with dos:
        lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_iYvSqSMKZB.json")
            
        st.subheader('¿No sabes por donde empezar?')
        st.info('¿Cual es tu tema de interes?')
        st.info('Documentate, investiga la información actual')
        st.info('¿Cual es la pregunta de investigación')
        st_lottie(lottie_hello,height=150)

    with tres:

        st.image('/Users/alonso/Focus/Imagenes/tesiscxcolcardio.png')
        st.info('Realiza tu proyecto de investigación en la modalidad y alcance que requieras en tiempo record')

    
elif seleccion=='Ingresa':
    seleccion1=option_menu(None,['Principal','Portada','Índice','Just','Hipo','Plant','M-T'],orientation='horizontal',icons=['journal-medical','card-list','type'])

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



