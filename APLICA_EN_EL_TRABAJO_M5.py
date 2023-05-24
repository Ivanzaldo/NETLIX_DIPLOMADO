#############################################################################################################
#PROYECTO: Aplica en el trabajo Modulo 5
#NOMBRE: Ivan Alejandro Anzaldo Baca
#FECHA: 23/05/2023
#############################################################################################################
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

st.set_page_config(page_title="Dashboard RETO", 
                   page_icon='🧑‍💼', 
                   layout="centered", 
                   initial_sidebar_state="auto", 
                   menu_items={'About': "# This is a header. This is an *extremely* cool app!"})
# Inicio
st.title('EMPLOYEES DASHBOARD')
st.header('Pequeña descripción')
st.markdown("""<p>Este dashboard permite mostrar el dataframe completo, igualmente filtrar por:</p>
<ul>
    <li>Employee_ID.&nbsp;</li>
    <li>Hometown.</li>
    <li>Unit.</li>
    <li>Education Level.</li>
</ul>
<p>Igualmente muestra 5 gr&aacute;ficas entre ellas:</p>
<ul>
    <li>Histograma de los empleados.</li>
    <li>Gr&aacute;fica de frecuencias por unidad funcional.</li>
    <li>Gr&aacute;fica de edad vs tasa de deserci&oacute;n.</li>
    <li>Gr&aacute;fica de tiempo de servicion vs tasa de deserci&oacute;n.</li>
    <li>Indice de deserci&oacute;n por ciudad.</li>
</ul>""", unsafe_allow_html=True)
# Funciones 
@st.cache
def load_data(nrows = 500):
    data = pd.read_csv('Employees.csv', nrows=nrows)
    return data  
@st.cache
def filtro1(tipo_busqueda,radio_1,text_input_1):
    data = pd.read_csv('Employees.csv')
    if tipo_busqueda == 'Contiene':
        data = data[data[radio_1].str.lower().str.contains(text_input_1.lower())]
    elif tipo_busqueda == 'Exacta':
        data = data[data[radio_1] == text_input_1]

    return data 
@st.cache
def filtro2(columna,selectbox_1):
    data = pd.read_csv('Employees.csv')
    data = data[data[columna] == selectbox_1]
    return data 
def unicos(columna):
    data = pd.read_csv('Employees.csv')
    return data[columna].unique() 

# Creacion del sidebar
employees_df = load_data(500)
sidebar = st.sidebar
sidebar.markdown("<h1 style='text-align: center; color: green;'>Sidebar filters</h1>", unsafe_allow_html=True)
sidebar.markdown('___')
checkbox_1 = sidebar.checkbox('Mostrar dataframe')
sidebar.markdown('___')
radio_1 = sidebar.radio("Seleccionar por que columna quieres filtrar 👉",
                        options=["Employee_ID", "Hometown", "Unit"],
                    )
radio_2 = sidebar.radio("Seleccionar el tipo de busqueda que quieres 👉",
                        options=["Exacta", "Contiene"],
                    )
text_input_1 = sidebar.text_input('Ingresa por elemento que quieres filtrar:',radio_1)
Filtrar_1 = sidebar.button('Filtrar')
sidebar.markdown('___')
selectbox_1   = sidebar.selectbox('Seleccionar nivel educativo', unicos('Education_Level') )
Filtrar_2 = sidebar.button('Filtrar', key='2')
sidebar.markdown('___')
selectbox_2   = sidebar.selectbox('Seleccionar la ciudad', unicos('Hometown') )
Filtrar_3 = sidebar.button('Filtrar', key='3')
sidebar.markdown('___')
selectbox_3   = sidebar.selectbox('Seleccionar la unidad funcional', unicos('Unit') )
Filtrar_4 = sidebar.button('Filtrar', key='4')
sidebar.markdown('___')
# Condiciones sidebar
if(checkbox_1):
    st.header('DataFrame Total')
    st.dataframe(employees_df)
elif(Filtrar_1):
    st.header('DataFrame Filtrado')
    dataframe_filtrar_1 = filtro1(radio_2,radio_1,text_input_1)
    st.dataframe(dataframe_filtrar_1)
    st.write('El total de empleados es: '+str(dataframe_filtrar_1.shape[0]))
elif(Filtrar_2):
    st.header('DataFrame Filtrado Nivel Educativo')
    dataframe_filtrar_2 = filtro2('Education_Level',selectbox_1)
    st.dataframe(dataframe_filtrar_2)
    st.write('El total de empleados es: '+str(dataframe_filtrar_2.shape[0]))
elif(Filtrar_3):
    st.header('DataFrame Filtrado Ciudad')
    dataframe_filtrar_3 = filtro2('Hometown',selectbox_2)
    st.dataframe(dataframe_filtrar_3)
    st.write('El total de empleados es: '+str(dataframe_filtrar_3.shape[0]))
elif(Filtrar_4):
    st.header('DataFrame Filtrado por Unidad')
    dataframe_filtrar_4 = filtro2('Unit',selectbox_3)
    st.dataframe(dataframe_filtrar_4)
    st.write('El total de empleados es: '+str(dataframe_filtrar_4.shape[0]))
else:
    pass

#Graficas
c1, c2= st.columns((1, 1))
#hist
c1.header('Histograma de los empleados')
employees = load_data(7000)
fig1, ax = plt.subplots()
employees['Age'].hist(ax = ax)
plt.xticks([19,23.6,28.2,32.8,37.4,42,46.6,51.2,55.8,60.4,65])
c1.pyplot(fig1)
# frecuencias por unit
c2.header('Gráfica de frecuencias por unidad funcional')
fig2, ax2 = plt.subplots()
sns.countplot(x = employees['Unit'], ax=ax2)
plt.xticks(rotation=90)
c2.pyplot(fig2)
# Scatter plots
c1, c2= st.columns((1, 1))
fig4, ax4 = plt.subplots()
fig5, ax5 = plt.subplots()
employees.plot.scatter(x='Age', y='Attrition_rate', ax = ax4, title = 'Age and Attrition_rate')
employees.plot.scatter(x='Time_of_service', y='Attrition_rate', ax = ax5, title = 'Time_of_service and Attrition_rate')
c1.header('Gráfica de edad vs tasa de deserción')
c2.header('Gráfica de tiempo de servicion vs tasa de deserción')
c1.pyplot(fig4)
c2.pyplot(fig5)
# desercion por ciudad
st.header('Indice de deserción por ciudad')
fig3, ax3 = plt.subplots()
employees_by_hometown = employees.groupby('Hometown')['Attrition_rate'].mean()
employees_by_hometown.plot(ax=ax3)
plt.xticks(rotation=90)
st.pyplot(fig3)
