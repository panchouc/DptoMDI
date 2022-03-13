import pandas as pd
import plotly.express as px
import streamlit as st
from classes import LecturaArchivos

archivo_display = "Gastos totales Marzo.xlsx"
file = pd.read_excel(archivo_display)
archivo_calculos = LecturaArchivos("Marzo_2022.xlsx", "Marzo")

datos = archivo_calculos.resumen_total()

parcial_feli_df = file[file["Persona"] == "Felipe"]
parcial_fco_df = file[file["Persona"] == "Francisco"]

total_feli_df = ""
total_fco_df = ""


try:
    frames_fco = [file[file["Persona"] == "Francisco"], file[file["Persona"] == "Solo Francisco"]]
    total_fco_df = pd.concat(frames_fco)

    frames_felipe = [file[file["Persona"] == "Felipe"], file[file["Persona"] == "Solo Felipe"]]
    total_feli_df = pd.concat(frames_felipe)
    
except:
    print("Algo ha salido mal")

parcial_feli = float(parcial_feli_df["Precio"].sum())
parcial_fco = float(parcial_fco_df["Precio"].sum())

total_feli = float(total_feli_df["Precio"].sum())
total_fco = float(total_fco_df["Precio"].sum())



st.set_page_config(page_title="Contabilidad",
                   page_icon = ":moneybag:",
                   layout="wide")

#SIDEBAR
st.sidebar.header("Ingresa los filtros aquí: ")

categoria = st.sidebar.multiselect(
    "Ingresa la categoría:",
    options = file["Categoria"].unique(),
    default = file["Categoria"].unique()
                                   )

persona = st.sidebar.multiselect(
    "Selecciona la persona: ",
    options= file["Persona"].unique(),
    default = file["Persona"].unique()
)


file_selection = file.query(
    "Categoria == @categoria & Persona == @persona"
)

st.title("Gastos del mes")
st.dataframe(file_selection, 2000, 1000)


#MAINPAGE

st.title(":chart_with_downwards_trend: Estadística")
st.markdown("##")


#TOP KPI'S
left_column, middle_column, right_column = st.columns(3)
cantidad = 0
persona = ""
recibidor = ""

if (parcial_feli / 2) > (parcial_fco / 2):
    cantidad = (parcial_feli / 2) - (parcial_fco / 2)
    persona = "Francisco"
    recibidor = "Felipe"
else:
    cantidad = (parcial_fco / 2) - (parcial_feli / 2)
    persona = "Felipe"
    recibidor = "Francisco"

with left_column:
    st.subheader("Gastos parciales Felipe")
    st.subheader(f"{parcial_feli} CLP")
    st.subheader("Gastos totales Felipe")
    st.subheader(f"{total_feli}")

with middle_column:
    st.subheader("Gastos parciales Francisco")
    st.subheader(f"{parcial_fco} CLP")
    st.subheader("Gastos totales Francisco")
    st.subheader(f"{total_fco}")

with right_column:
    st.subheader(f"{persona} debe a {recibidor}")
    st.subheader(f"{cantidad}")

st.markdown("---------")


st.title("Gastos en orden descendente")
orden = file.sort_values("Precio", ascending=False)
st.dataframe(orden, 2000, 1000)