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

acteur = st.selectbox('Choisir un acteur', df_acteur['acteur'])
score_acteur = df_acteur[df_acteur['acteur'] == acteur]['score_acteur'].values[0]




