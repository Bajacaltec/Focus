from boto import config
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from matplotlib.pyplot import title
import streamlit as st
import sqlite3
import pandas as pd
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide',page_title='Haz tu tesis')
# revisar este como nicial
#Menu#
# modificación del menú#
#iconos poner el nombre de bootstrap
# with st.sidebar: (ponerlo en el sidebar)



seleccion=option_menu(None,['Portada','Índice','Just','Hipo','Plant','M-T'],orientation='horizontal',icons=['journal-medical','card-list','type'])

def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
            
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



