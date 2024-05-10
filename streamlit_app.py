import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import plotly.graph_objects as go




st.set_page_config(page_title="Projet Ciné", layout="wide") 

st.title("L'IA au service de la production cinématographique !")

st.sidebar.title("Sommaire")
pages=["Présentation du projet", "Collecte et Exploration des Données", "Analyse des Données (DataViz)", "Préparation les données - Preprocessing", "Présentation du modèle", "DEMONSTRATION"]
page=st.sidebar.radio("Aller vers", pages)


if page == pages[0] : 

    col1, col2 = st.columns(2)

    with col1:
        st.image('images/cinema.jpg')

    with col2:
        st.write("### Le contexte :")
        st.write("Le projet que nous présentons dans ce document est le fruit de notre propre initiative. Inspiré par une idée originale d'un des membres de notre groupe, ce projet s'est développé autour d'une ambition commune : transformer radicalement l'industrie du cinéma !")
        st.write("Traditionnellement, il est courant que les producteurs et les professionnels du cinéma fassent des paris amicaux sur le nombre de spectateurs qu'un film attirera à la fin de sa première semaine en salle. Cette pratique, à la fois ludique et ancrée dans les mœurs du secteur, a été le catalyseur de notre projet. Notre objectif est de mettre au point un modèle de machine learning capable de prédire avec la plus grande précision possible le nombre d'entrées qu'un film réalisera. Ce modèle s'appuiera sur des données préalablement collectées, alliant des critères quantitatifs et qualitatifs pour établir ses prévisions.")
    
        st.write("### L'objectif du projet :")
        st.write("L'objectif central de notre projet est de développer un outil accessible et convivial, permettant à tout utilisateur de prévoir le nombre de spectateurs d'un film à la fin de sa première semaine en salle. En renseignant des paramètres spécifiques de son choix, l'utilisateur pourra obtenir rapidement une estimation précise des entrées en salle.")
        st.write("### Pourquoi avoir choisi streamlit ?")
        st.write("Au-delà des fonctionnalités de base de cet applicatif, qui contribuent à rendre nos présentations plus dynamiques et visuellement impactantes, il est important de souligner que le choix de Streamlit pour présenter notre projet a également répondu à plusieurs objectifs pédagogiques. En effet, Streamlit est un outil de plus en plus prisé au sein des entreprises.")
        st.write("En intégrant Streamlit, nous avons non seulement amélioré l'interactivité et l'impact visuel de notre présentation, mais aussi enrichi notre expérience d'apprentissage avec une application technologique en pleine expansion. Cette démarche nous a permis de nous approprier efficacement cet outil moderne, en vue de l'utiliser plus tard dans nos futures carrières.")
    

if page == pages[1] : 
    st.write("### Notre jeu de donnée lors du démarrage et son évolution")
    st.write("Au cours de l'analyse initiale de notre jeu de données et à la lumière de nos premiers acquis en matière de formation, nous avons constaté que nos données étaient insuffisantes pour élaborer un modèle de machine learning robuste. Plusieurs défis se sont présentés : d'abord, notre jeu de données contenait un nombre excessif de valeurs manquantes. De plus, nous hésitions encore sur la variable cible à prédire, hésitant entre les revenus générés et les votes des spectateurs.")       
    st.write("Par ailleurs, notre jeu de données couvrait le marché mondial, ce qui nous a rapidement motivé a nous focaliser sur le marché français, necessitant de trouver de nouvelles sources de données.")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('images/Heatmap_NaN.png')
    st.write("Pour enrichir notre base, nous avons mis en place plusieurs actions :")
    st.write("‣ Nous avons contacté CBO BOX OFFICE, une société fournissant des données aux professionnels du cinéma. Malgré une proposition contractuelle exposant le contexte non lucratif et éducatif de notre projet, notre demande est restée sans réponse.")
    st.write("‣ Nous avons exploré d'autres plateformes telles que KAGGLE pour trouver des jeux de données robustes et adaptées à nos besoins, mais sans succès.")
    st.write("‣ Nous avons décidé de procéder au Webscraping de données sur des sites réputés bien administrés, tels qu'Allociné, IMDB PRO (gratuit le premier mois), et JPBOX Office. Avec le soutien de notre chef de cohorte, qui a débloqué un sprint complet dédié au web scraping, nous avons utilisé Beautiful Soup pour extraire et compléter notre jeu de données pour le marché français. Nous avons ainsi obtenu la liste des films sur Allociné avec leurs box-office et titres originaux, qui nous serviront plus tard comme clés d'indexation. Nous avons enrichi ces films avec des caractéristiques telles que la note des spectateurs, la note de la presse, les acteurs principaux, les réalisateurs, les scénaristes, les distributeurs, la date de sortie, la nationalité, le budget et le genre.")
    st.write("‣ Sur IMDB, nous avons récupéré un fichier global contenant les identifiants IMDB des films, leur durée et leurs titres originaux (toujours dans l'optique de l'utiliser comme clé d'indexation).")
    st.write("‣ Enfin, nous avons décidé de scraper sur IMDB et Allociné des données permettant de construire un score de notoriété pour chaque acteur, réalisateur ou scénariste, en nous basant sur le Starmeter, le nombre de récompenses reçues, le nombre de films réalisés et la durée de leur carrière.")
    st.write("Ces démarches nous ont permis de bâtir un jeu de données plus complet et pertinent pour le développement de notre modèle prédictif du nombre d'entrées sur le marché français.")
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image('images/Schema_budget.png')
   

    
if page == pages[2] :
    allocine = pd.read_csv('data/allocine_V1.csv')
    pays_counts = allocine['pays'].dropna().value_counts()
    top_pays = pays_counts[:8]
    autres = pays_counts[8:].sum()
    top_pays['Autres'] = autres
    
    fig = go.Figure(data=[go.Pie(labels=top_pays.index, values=top_pays.values, hole=.3)])
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(
    width=800,
    height=600,
    title_text='Répartition des films par pays',
    annotations=[dict(text='Pays', x=0.5, y=0.5, font_size=20, showarrow=False)],
    legend_title="Pays"
    )
    st.plotly_chart(fig)

    

if page == pages[3] :
    st.write("")
    st.image('images/score_acteur.png')
