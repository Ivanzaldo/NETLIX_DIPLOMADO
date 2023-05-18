import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.set_page_config(page_title="Dashboar Netflix", 
                   page_icon='🎥', 
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   menu_items={'About': "# This is a header. This is an *extremely* cool app!"})
###########################################################################################################################
########################################## UPLOAD DATA START ##############################################################
###########################################################################################################################

image_netflix = Image.open('imagenes/netflix.jpg')
c1, c2= st.columns((1, 5))
c1.image(image_netflix)
c2.title('NETFLIX DASHBOARD')

st.markdown("<h2 style='text-align: center; color: red;'>Todos los filmes</h2>", unsafe_allow_html=True)
    

@st.cache
def load_data(nrows):
    data = pd.read_csv('movies.csv', encoding = "ISO-8859-1", nrows=nrows)
    return data   

data = load_data(500)
sidebar = st.sidebar
checkbox_1 = sidebar.checkbox('Mostrar todos los filmes')
title = sidebar.text_input('Ingresa el titulo del filme:','Titulo')
Buscar_filmes = sidebar.button('Buscar filmes')

Director_seleccionar   = sidebar.selectbox('Seleccionar director', data['director'].unique())
Filtrar_director = sidebar.button('Filtrar director')

if(checkbox_1):
    st.dataframe(data)
if(Buscar_filmes):
    st.dataframe(data[data['name'].str.lower().str.contains(title.lower())])
if(Filtrar_director):
    st.dataframe(data[data['director']==Director_seleccionar])

    












    







    




    


    



