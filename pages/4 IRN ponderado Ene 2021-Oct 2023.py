# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:03:48 2023

@author: jperezr
"""

import pandas as pd
import numpy as np
import streamlit as st

# Data import & columns
df = pd.read_csv('Libro4.csv')

#df['90s'] = df['minutes']/90

#calc_elements = ['goals', 'assists', 'points']

#for each in calc_elements:
#    df[f'{each}_p90'] = df[each] / df['90s']

#positions = list(df['position'].drop_duplicates())
AFORE = list(df['AFORE'].drop_duplicates())

Fecha = list(df['Fecha'].drop_duplicates())

# App

# Sidebar - title & filters
st.sidebar.markdown('### Filtro de datos')
AFORE_choice = st.sidebar.multiselect(
    'Elige una AFORE:', AFORE, default=AFORE)


Fecha_choice = st.sidebar.multiselect(
    "Elige una Fecha:", Fecha, default=Fecha)


#price_choice = st.sidebar.slider(
#    'Max Price:', min_value=4.0, max_value=15.0, step=.5, value=15.0)


df = df[df['AFORE'].isin(AFORE_choice)]
df = df[df['Fecha'].isin(Fecha_choice)]

#df = df[df['cost'] < price_choice]

# Main
st.title(f"IRN ponderado por mes")
st.header("ene-2021 a oct-2023")
st.subheader("Ranking")

# Main - dataframes
st.markdown('### Cuadro de datos')


s = df.style.format({"Expense": lambda x : '{:.4f}'.format(x)})
st.dataframe(s)

#st.dataframe(df.sort_values('Suma IRN',
#             ascending=False).reset_index(drop=True))
