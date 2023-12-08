# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:22:19 2023

@author: jperezr
"""

import pandas as pd
import numpy as np
import streamlit as st

# Data import & columns
df = pd.read_csv('Libro1.csv')

#df['90s'] = df['minutes']/90

#calc_elements = ['goals', 'assists', 'points']

#for each in calc_elements:
#    df[f'{each}_p90'] = df[each] / df['90s']

#positions = list(df['position'].drop_duplicates())
AFORE = list(df['AFORE'].drop_duplicates())

SIEFORE = list(df['SIEFORE'].drop_duplicates())

Fecha = list(df['Fecha'].drop_duplicates())

# App

# Sidebar - title & filters
st.sidebar.markdown('### Filtro de datos')
AFORE_choice = st.sidebar.multiselect(
    'Elige una AFORE:', AFORE, default=AFORE)

SIEFORE_choice = st.sidebar.multiselect(
    "Elige una SIEFORE:", SIEFORE, default=SIEFORE)

Fecha_choice = st.sidebar.multiselect(
    "Elige una Fecha:", Fecha, default=Fecha)


#price_choice = st.sidebar.slider(
#    'Max Price:', min_value=4.0, max_value=15.0, step=.5, value=15.0)


df = df[df['AFORE'].isin(AFORE_choice)]
df = df[df['SIEFORE'].isin(SIEFORE_choice)]
df = df[df['Fecha'].isin(Fecha_choice)]

#df = df[df['cost'] < price_choice]

# Main
st.title(f"IRN ene-2021 a oct-2023")

# Main - dataframes
st.markdown('### Cuadro de datos')

st.dataframe(df.sort_values('IRN',
             ascending=False).reset_index(drop=True))

