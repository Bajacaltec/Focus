from boto import config
from matplotlib.ft2font import HORIZONTAL, VERTICAL
from matplotlib.pyplot import title
import streamlit as st
import psycopg2
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide',page_title='Haz tu tesis')
#Menu#
# modificación del menú#
#iconos poner el nombre de bootstrap
# with st.sidebar: (ponerlo en el sidebar)
st.write('Prueba de upload')
#Base render
conn = psycopg2.connect("dbname=base_vhom user=base_vhom_user password=8xUvM1YA3iw7Rjb1FxPTkgRf2xEFl87T host=dpg-cggclf02qv28tc396eng-a Port=5432")

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
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



