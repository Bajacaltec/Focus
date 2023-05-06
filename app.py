       
import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from contacto import contacto
from dinero import money
from asesores import alonso
import numpy as np
import time
from principal import main
import base64
st.set_page_config(layout='wide',page_title='Tess extractor',menu_items=None,page_icon='Tessextractor', )

####
# encabezado y menú
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
tol1,tol2,tol3=st.columns([1,2,1])
with tol1:
    teesextractor=load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_yheqnvx7.json')
    st_lottie(teesextractor,height=100)
with tol2:
    st.write('')
    st.write('')
    st.caption('By Nunztec')
with tol3:
    mex=load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_jidselhy.json')
    st_lottie(mex,height=50)
    
    
seleccion=option_menu(None,['Principal','Contacto','Costos','Privacidad'],orientation='horizontal',icons=['journal-medical','bi bi-headset','','bi bi-cash-coin'], styles={
        "container": {"padding": "0!important", "background-color": "#E5EFF6"},
        "icon": {"color": "black", "font-size": "23px"}, 
        "nav-link": {"font-size": "18px", "text-align": "Center", "margin":"0px", "--hover-color": "#D3EA8B"},
        "nav-link-selected": {"background-color": "#407BD2"},
    })

#Principal#
if seleccion=='Principal':
    main()



#Editores

elif seleccion=='Editores':
    alonso()
          



#Contacto#
elif seleccion=='Contacto':
    contacto()


 
 
elif seleccion=='Costos':
    money()


elif seleccion=='Privacidad':
    st.write("""Política de Privacidad

Fecha de entrada en vigor: 06.05.23

Esta Política de Privacidad describe cómo se recopila, utiliza y comparte la información personal de los usuarios ("usted" o "el usuario") al utilizar nuestros servicios. Por favor, lea detenidamente esta política antes de utilizar nuestro sitio web o cualquier otro servicio relacionado ("servicios").

Información que recopilamos
Podemos recopilar la siguiente información personal cuando usted utiliza nuestros servicios:
1.1. Información proporcionada por usted: Podemos recopilar la información que usted nos proporciona cuando crea una cuenta, se comunica con nosotros o utiliza nuestros servicios. Esto puede incluir su nombre, dirección de correo electrónico, número de teléfono y otra información similar.

1.2. Información de uso: Recopilamos información sobre cómo usted utiliza nuestros servicios, incluyendo la fecha y hora de acceso, las páginas que visita, las características a las que accede y cualquier acción realizada durante su interacción con los servicios.

1.3. Información del dispositivo: Podemos recopilar información sobre el dispositivo que utiliza para acceder a nuestros servicios, incluyendo el tipo de dispositivo, la dirección IP, el sistema operativo, el identificador único del dispositivo y otra información similar.

Uso de la información recopilada
Utilizamos la información recopilada para los siguientes propósitos:
2.1. Proporcionar y mejorar nuestros servicios: Utilizamos la información para proporcionarle los servicios solicitados y mejorar continuamente su experiencia de uso.

2.2. Comunicaciones: Podemos utilizar su información para enviarle comunicaciones relacionadas con nuestros servicios, como actualizaciones del sistema, notificaciones importantes o información promocional. Usted tiene la opción de optar por no recibir ciertos tipos de comunicaciones.

2.3. Seguridad: Utilizamos la información para garantizar la seguridad de nuestros servicios y de los usuarios, así como para detectar y prevenir actividades fraudulentas o no autorizadas.

2.4. Cumplimiento legal: Podemos utilizar la información para cumplir con nuestras obligaciones legales, como responder a solicitudes legales o cooperar en investigaciones legales.

Compartir información con terceros
Podemos compartir su información personal con terceros en las siguientes circunstancias:
3.1. Proveedores de servicios: Podemos compartir su información con proveedores de servicios que realizan funciones en nuestro nombre, como el procesamiento de pagos, el envío de correos electrónicos o el análisis de datos. Estos proveedores de servicios están obligados a proteger la información y solo pueden utilizarla de acuerdo con nuestras instrucciones.

3.2. Cumplimiento legal y protección de derechos: Podemos compartir información cuando creemos de buena fe que la divulgación es necesaria para cumplir con una obligación legal, proteger nuestros derechos o los derechos de otros usuarios, investigar fraudes o responder a solicitudes gubernamentales.

3.3. Consentimiento: También podemos compartir su información personal con terceros cuando usted nos ha dado su consentimiento para hacerlo.

Seguridad de la información
Tomamos medidas razonables para proteger la información personal contra pérdida, robo, uso no autorizado o acceso no autorizado. Sin embargo, no podemos garantizar la seguridad absoluta de la información.
Retención de la información
Retendremos su información personal durante el tiempo necesario para cumplir con los fines establecidos en esta política, a menos que se requiera""")

st.markdown('________')
jol1,jol2,jol3=st.columns([1,1,5])
with jol1:
    st.subheader('Contacto')
with jol2:
    hu=load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_twijbubv.json')
    st_lottie(hu,height=70)
col1,col2,colx=st.columns([3,1,1])
with col1:
    st.image('Imagenes/gmail.png',width=35)
    st.caption('elmedpost@gmail.com - Mdfnunez@gmail.com')


with col2:

    st.image('Imagenes/whatsapp.png',width=35)
    st.markdown('+529617024389')


    
with colx:
    st.empty()
    
st.markdown('_________')
st.caption('Tessextractor fue elaborado por Nunztec con el lenguaje de programación python y streamlit, para mayor información sobre nuestros productos, ingresa a la página de contacto y envianos un E mail')
