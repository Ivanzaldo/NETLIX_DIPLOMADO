import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as  plt
import seaborn as sns
from PIL import Image
import altair as alt

sns.set_theme(style="darkgrid")
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

df_movies_original = pd.read_csv('movies.csv', encoding = "ISO-8859-1")

#################################### COUNTRIES ##################################
my_expander1 = st.expander(label='COUNTRIES TABLES AND KPIS')

with my_expander1:

    c1, c2, c3,c4 = st.columns((1, 1, 1.1,1.4))
    
    c1.markdown("<h5 style='text-align: center; color: black;'>País con mas peliculas</h5>", unsafe_allow_html=True)
    c1.markdown("<h4 style='text-align: center; color: red;'>"+df_movies_original['country'].value_counts().index[0]+"</h4>", unsafe_allow_html=True)
    c1.markdown('___')
    c1.markdown("<h5 style='text-align: center; color: black;'>País con mas budget</h5>", unsafe_allow_html=True)
    c1.markdown("<h4 style='text-align: center; color: red;'>"+df_movies_original.groupby('country')['budget'].sum().sort_values(ascending=False).index[0]+"</h4>", unsafe_allow_html=True)
    c1.markdown('___')
    c1.markdown("<h5 style='text-align: center; color: black;'>País mejor evaluado</h5>", unsafe_allow_html=True)
    c1.markdown("<h4 style='text-align: center; color: red;'>"+df_movies_original.groupby('country')['score'].mean().sort_values(ascending=False).index[0]+"</h4>", unsafe_allow_html=True)
    c1.markdown('___')
    c2.markdown("<h5 style='text-align: center; color: black;'>Países con mas peliculas</h5>", unsafe_allow_html=True)
    df_paises_mas_peliculas = pd.DataFrame(df_movies_original['country'].value_counts())
    df_paises_mas_peliculas.columns = ['Cuenta']
    c2.dataframe(df_paises_mas_peliculas)

    c3.markdown("<h5 style='text-align: center; color: black;'>Países con mas budget</h5>", unsafe_allow_html=True)
    df_paises_mas_budget = pd.DataFrame(df_movies_original.groupby('country')['budget'].sum().sort_values(ascending=False))
    df_paises_mas_budget.columns = ['Budget']
    c3.dataframe(df_paises_mas_budget)

    c4.markdown("<h5 style='text-align: center; color: black;'>Países mejor evaluados</h5>", unsafe_allow_html=True)
    df_paises_mejor_evaluados = pd.DataFrame(df_movies_original.groupby('country')['score'].mean().sort_values(ascending=False))
    df_paises_mejor_evaluados.columns = ['Score']
    c4.dataframe(df_paises_mejor_evaluados)


#################################### GENERO ##################################
my_expander2 = st.expander(label='GENRE TABLES AND KPIS')

with my_expander2:
    c1, c2, c3,c4 = st.columns((1, 1, 1.1,1.4))
    
    c1.markdown("<h5 style='text-align: center; color: black;'>Genero con mas peliculas</h5>", unsafe_allow_html=True)
    c1.markdown("<h4 style='text-align: center; color: red;'>"+df_movies_original['genre'].value_counts().index[0]+"</h4>", unsafe_allow_html=True)
    c1.markdown('___')
    c1.markdown("<h5 style='text-align: center; color: black;'>Genero con mas budget</h5>", unsafe_allow_html=True)
    c1.markdown("<h4 style='text-align: center; color: red;'>"+df_movies_original.groupby('genre')['budget'].sum().sort_values(ascending=False).index[0]+"</h4>", unsafe_allow_html=True)
    c1.markdown('___')
    c1.markdown("<h5 style='text-align: center; color: black;'>Genero mejor evaluado</h5>", unsafe_allow_html=True)
    c1.markdown("<h4 style='text-align: center; color: red;'>"+df_movies_original.groupby('genre')['score'].mean().sort_values(ascending=False).index[0]+"</h4>", unsafe_allow_html=True)
    c1.markdown('___')
    c2.markdown("<h5 style='text-align: center; color: black;'>Generos con mas peliculas</h5>", unsafe_allow_html=True)
    df_paises_mas_peliculas = pd.DataFrame(df_movies_original['genre'].value_counts())
    df_paises_mas_peliculas.columns = ['Cuenta']
    c2.dataframe(df_paises_mas_peliculas.head(10))

    c3.markdown("<h5 style='text-align: center; color: black;'>Generos con mas budget</h5>", unsafe_allow_html=True)
    df_paises_mas_budget = pd.DataFrame(df_movies_original.groupby('genre')['budget'].sum().sort_values(ascending=False))
    df_paises_mas_budget.columns = ['Budget']
    c3.dataframe(df_paises_mas_budget.head(10))

    c4.markdown("<h5 style='text-align: center; color: black;'>Generos mejor evaluados</h5>", unsafe_allow_html=True)
    df_paises_mejor_evaluados = pd.DataFrame(df_movies_original.groupby('genre')['score'].mean().sort_values(ascending=False))
    df_paises_mejor_evaluados.columns = ['Score']
    c4.dataframe(df_paises_mejor_evaluados.head(10))
#################################### MOVIE ##################################
my_expander3 = st.expander(label='MOVIES TABLES AND KPIS')

with my_expander3:
    c1, c2 = st.columns((1,1))
    
    c1.markdown("<h5 style='text-align: center; color: black;'>Pelicula con mas budget</h5>", unsafe_allow_html=True)
    c1.markdown("<h6 style='text-align: center; color: red;'>"+df_movies_original.groupby('name')['budget'].sum().sort_values(ascending=False).index[0]+"</h6>", unsafe_allow_html=True)
    c1.markdown('___')
    c2.markdown("<h5 style='text-align: center; color: black;'>Pelicula mejor evaluada</h5>", unsafe_allow_html=True)
    c2.markdown("<h6 style='text-align: center; color: red;'>"+df_movies_original.groupby('name')['score'].mean().sort_values(ascending=False).index[0]+"</h6>", unsafe_allow_html=True)
    c2.markdown('___')
    cc1, cc2 = st.columns((1.2,.8))
    cc1.markdown("<h5 style='text-align: center; color: black;'>Peliculas con mas budget</h5>", unsafe_allow_html=True)
    df_paises_mas_budget = pd.DataFrame(df_movies_original.groupby('name')['budget'].sum().sort_values(ascending=False))
    df_paises_mas_budget.columns = ['Budget']
    cc1.dataframe(df_paises_mas_budget.head(10))

    cc2.markdown("<h5 style='text-align: center; color: black;'>Peliculas mejor evaluadas</h5>", unsafe_allow_html=True)
    df_paises_mejor_evaluados = pd.DataFrame(df_movies_original.groupby('name')['score'].mean().sort_values(ascending=False))
    df_paises_mejor_evaluados.columns = ['Score']
    cc2.dataframe(df_paises_mejor_evaluados.head(10))
#################################### ESTRELLA ##################################
my_expander4 = st.expander(label='DIRECTOR AND ACTOR TABLES AND KPIS')

with my_expander4:
    c1, c2 = st.columns((1,1))
    
    c1.markdown("<h5 style='text-align: center; color: black;'>Director with best movie score</h5>", unsafe_allow_html=True)
    c1.markdown("<h6 style='text-align: center; color: red;'>"+df_movies_original.groupby('director')['score'].sum().sort_values(ascending=False).index[0]+"</h6>", unsafe_allow_html=True)
    c1.markdown('___')
    c2.markdown("<h5 style='text-align: center; color: black;'>Actor with best movie score</h5>", unsafe_allow_html=True)
    c2.markdown("<h6 style='text-align: center; color: red;'>"+df_movies_original.groupby('star')['score'].mean().sort_values(ascending=False).index[0]+"</h6>", unsafe_allow_html=True)
    c2.markdown('___')
    cc1, cc2 = st.columns((1,1))
    cc1.markdown("<h5 style='text-align: center; color: black;'>Directors with best movie score</h5>", unsafe_allow_html=True)
    df_paises_mas_budget = pd.DataFrame(df_movies_original.groupby('director')['score'].sum().sort_values(ascending=False))
    df_paises_mas_budget.columns = ['Score']
    cc1.dataframe(df_paises_mas_budget.head(10))

    cc2.markdown("<h5 style='text-align: center; color: black;'>Actors with best movie score</h5>", unsafe_allow_html=True)
    df_paises_mejor_evaluados = pd.DataFrame(df_movies_original.groupby('star')['score'].mean().sort_values(ascending=False))
    df_paises_mejor_evaluados.columns = ['Score']
    cc2.dataframe(df_paises_mejor_evaluados.head(10))
#################################### GRAFICAS ##################################
my_expander5 = st.expander(label='GENERAL GRAPHS')

with my_expander5:
    st.markdown("<h5 style='text-align: center; color: black;'>Movies by year</h5>", unsafe_allow_html=True)
    
    movies_by_year=pd.DataFrame(df_movies_original['year'].value_counts().sort_values())
    movies_by_year.columns = ['Movies by year']
    st.line_chart(movies_by_year)
    st.markdown("<h5 style='text-align: center; color: black;'>Budget by year</h5>", unsafe_allow_html=True)
    
    budget_by_year=pd.DataFrame(df_movies_original.groupby('year')['budget'].sum().sort_values(ascending=False))
    budget_by_year.columns = ['Budget by year']
    st.line_chart(budget_by_year)

    st.markdown("<h5 style='text-align: center; color: black;'>Budget by genre</h5>", unsafe_allow_html=True)
    budget_by_genre = pd.DataFrame(df_movies_original.groupby('genre')['budget'].mean().sort_values(ascending=False))
    st.bar_chart(budget_by_genre)

    st.markdown("<h5 style='text-align: center; color: black;'>Correlation generator</h5>", unsafe_allow_html=True)
    c1, c2 = st.columns((1,1))
    lista_opciones = ['year', 'score', 'votes','budget']
    option1 = c1.selectbox('Inserta el primer feature numerico',lista_opciones)
    #lista_opciones.remove(option1)
    option2 = c1.selectbox('Inserta el segundo feature numerico',lista_opciones)

    temp_correlation = pd.DataFrame(df_movies_original[[option1,option2]])
    #temp_correlation.set_index(option1,inplace =True)

    

    chart = alt.Chart(temp_correlation).mark_circle().encode(
                    x=option1,
                    y=option2,
                                            ).interactive()
    st.altair_chart(chart, use_container_width=True)
    




    


    



