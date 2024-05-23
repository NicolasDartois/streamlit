import streamlit as st
import joblib as jl
import pandas as pd
from include.css_and_credit import css_and_credit

css_and_credit()

st.header("🎬Démonstration🎬")

model = jl.load("models/GB.joblib")

df_acteur = pd.read_csv('data/score_acteur.csv')
df_real = pd.read_csv('data/score_real.csv')
df_scenar = pd.read_csv('data/score_scenar.csv')

acteur1 = st.selectbox('Choisir l\'acteur principal :', df_acteur['Acteur'])
score_acteur1 = df_acteur[df_acteur['Acteur'] == acteur1]['Score'].values[0]
st.write(score_acteur1)

acteur2 = st.selectbox('Choisir l\'acteur principal :', df_acteur['Acteur'])
score_acteur2 = df_acteur[df_acteur['Acteur'] == acteur2]['Score'].values[0]
st.write(score_acteur2)
st.write((score_acteur1*1.125)+(score_acteur2*0.75))




