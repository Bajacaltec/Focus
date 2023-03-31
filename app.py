       
from turtle import width
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from matplotlib.pyplot import title
import streamlit as st
import requests
import matplotlib.pyplot as plt
import json
from streamlit_lottie import st_lottie
import psycopg2
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide',page_title='Haz tu tesis',menu_items=None,page_icon='Doit')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
tol1,tol2,tol3=st.columns([1,2,1])
with tol1:
    teesextractor=load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_yheqnvx7.json')
    st_lottie(teesextractor,height=150)
with tol2:
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.caption('By Nunztec')



seleccion=option_menu(None,['Principal','Contacto','Pago','Ingresa'],orientation='horizontal',icons=['journal-medical','card-list','type'])

if seleccion=='Principal':
    

    
        
        

    uno,dos,tres=st.columns([1,2,1])
    with uno:
        lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_iYvSqSMKZB.json")
        st_lottie(lottie_hello,height=150) 

        

        st.image('/Users/alonso/Focus/Imagenes/posterneurospora.png')
        st.info('Poster para congreso de ciencias biológicas')
        st.image('/Users/alonso/Focus/Imagenes/articulocureus.png')
        st.success('Reporte de caso de necrosis gástrica publicado en revista Cureus en idioma inglés')
        
    with dos:
        st.subheader('¿No sabes por donde empezar?')
        st.success('Con nuestra guía terminarás tu proyecto en el menor tiempo posible, con el menor dolor de cabeza posible, y con la mejor calidad posible.')
        st.warning('Realiza tu protocolo de investigación con un asesor directamente trabajando contigo lado a lado.')
        st.warning('Diseño metodológico adecuado, los errores de ejecución se eliminan o disminuyen con un buen diseño metodológico.')
        st.warning('Análisis estadístico preciso y adecuado con el lenguaje R.')
        st.warning('Apoyo en la redacción y traducción de tesis para publicación')
        st.video('/Users/alonso/Focus/Imagenes/cxcorazon.mp4',start_time=0)
        st.error('Video 1. Toracotomia anterolateral izquierda con pericardiotomía y exposición de miocardio. Cirugía por trauma penetrante de tórax por proyectil de arma de fuego en hospital de traumatología Lomas Verdes IMSS')
       
        

    with tres:
        mex=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_jidselhy.json')
        st_lottie(mex,height=50)
        st.write('¿Qué es la investigación, sino una cita a ciegas con el conocimiento? ')
        st.latex('Will Harvey')
        lotbook=load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_tnrzlN.json')
        st_lottie(lotbook)
        st.info('Realiza tu proyecto de investigación en la modalidad y alcance que requieras en tiempo record')
        st.image('/Users/alonso/Focus/Imagenes/tesiscxcolcardio.png')
        st.success('Utilizamos el lenguaje R para el análisis estadístico y programación con python para hacer mas fácil tu proceso de desarrollo de tu proyecto de investigación, no necesitas nada mas que nuestra orientación y herramientas')
        st.image('/Users/alonso/Focus/Imagenes/logo.jpeg')
        st.subheader('Visita el Medpost un diario de salud con las noticias más actuales')
        st.markdown('https://elmedpost.wordpress.com')
        st.image('/Users/alonso/Focus/Imagenes/Webapp medpost.png')
        st.subheader('Utiliza nuestras Webapps')

        

#Contacto#
elif seleccion=='Contacto':
    col1,col2=st.columns(2)
    with col1:
        contact_form = """
        <form action="https://formsubmit.co/mdfnunez@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        
        <input type="email" name="email" placeholder="Tu correo electrónico (email)" required>
        <input type="text" name="Número de telefono (opcional)" placeholder="Número de teléfono" >

        <input type="text" name="name" placeholder="¿Cual es tu nombre?" required>
        <textarea name="message" placeholder="¿En que podemos ayudarte?"></textarea>
        <input type="hidden" name="_next" value="http://192.168.1.103:8501">
        <button type="submit">Enviar</button>
        </form>
        """
        mail='Contactanos <i class="bi bi-mailbox"></i>'
        st.header('Contactanos :mailbox_closed:')
        st.markdown(contact_form, unsafe_allow_html=True)
         # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        local_css("style/style.css")
    with col2:
        pollo=load_lottieurl('https://assets10.lottiefiles.com/packages/lf20_se3w0ukg.json')
        st_lottie(pollo)

       

 
elif seleccion=='Pago':
    st.write('pagar')
    
elif seleccion=='Ingresa':
    st.balloons()
    
    seleccion1=option_menu(None,['Portada','Índice','Just','Hipo','Plant','M-T','Resultados','Graficos','Figuras','Conclusiones','Discusión','Referencias'],orientation='horizontal',icons=['journal-medical','card-list','type'])
    if seleccion1=='Portada':
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



