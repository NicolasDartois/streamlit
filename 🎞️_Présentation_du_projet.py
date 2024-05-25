import streamlit as st
import streamlit.components.v1 as components
from include.css_and_credit import css_and_credit

st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")
st.markdown("""<div class ="centered-content"><h1>🎥 L'IA au service de la production cinématographique ! 🎥</h1></div>""", unsafe_allow_html=True)

css_and_credit()

st.markdown("""<div class ="centered-content"><div class="box"><h3>Le contexte :</h3>
  <p>Le projet que nous présentons dans ce document est le fruit de notre propre initiative. Inspiré par une idée originale d\'un des membres de notre groupe, ce projet s\'est développé autour d\'une ambition commune : transformer radicalement l\'industrie du cinéma !</p>
  <p>Traditionnellement, il est courant que les producteurs et les professionnels du cinéma fassent des paris amicaux sur le nombre de spectateurs qu\'un film attirera à la fin de sa première semaine en salle. 
    Cette pratique, à la fois ludique et ancrée dans les mœurs du secteur, a été le catalyseur de notre projet. Notre objectif est de mettre au point un modèle de machine learning capable de prédire avec la plus grande précision possible le nombre d\'entrées qu\'un film réalisera. 
    Ce modèle s\'appuiera sur des données préalablement collectées, alliant des critères quantitatifs et qualitatifs pour établir ses prévisions.</p></div></div>""", unsafe_allow_html=True)

st.markdown("""<div class ="centered-content"><div class="box"><h3>L\'objectif du projet :</h3>
  <p>L\'objectif central de notre projet est de développer un outil accessible et convivial, permettant à tout utilisateur de prévoir le nombre de spectateurs d\'un film à la fin de sa première semaine en salle. 
    En renseignant des paramètres spécifiques de son choix, l\'utilisateur pourra obtenir rapidement une estimation précise des entrées en salle.</p></div></div>""", unsafe_allow_html=True)

st.markdown("""<div class ="centered-content"><div class="box"><h3>Pourquoi avoir choisi Streamlit ?</h3>
  <p>Au-delà des fonctionnalités de base de cet applicatif, qui contribuent à rendre nos présentations plus dynamiques et visuellement impactantes, il est important de souligner que le choix de Streamlit pour présenter notre projet a également répondu à plusieurs objectifs pédagogiques. 
    En effet, Streamlit est un outil de plus en plus prisé au sein des entreprises.</p>
  <p>En intégrant Streamlit, nous avons non seulement amélioré l\'interactivité et l\'impact visuel de notre présentation, mais aussi enrichi notre expérience d\'apprentissage avec une application technologique en pleine expansion. 
    Cette démarche nous a permis de nous approprier efficacement cet outil moderne, en vue de l\'utiliser plus tard dans nos futures carrières.</p></div></div>""", unsafe_allow_html=True)

st.markdown("""
<div class="centered-content">
    <div class="tab-container">
        <div class="tab-buttons">
            <button class="tab-link active" onclick="openTab(event, 'Contexte')">Le contexte</button>
            <button class="tab-link" onclick="openTab(event, 'Objectif')">L'objectif du projet</button>
            <button class="tab-link" onclick="openTab(event, 'Streamlit')">Pourquoi avoir choisi Streamlit ?</button>
        </div>
        <div id="Contexte" class="tab-content active">
            <div class="box">
                <h3>Le contexte :</h3>
                <p>Le projet que nous présentons dans ce document est le fruit de notre propre initiative. Inspiré par une idée originale d'un des membres de notre groupe, ce projet s'est développé autour d'une ambition commune : transformer radicalement l'industrie du cinéma !</p>
                <p>Traditionnellement, il est courant que les producteurs et les professionnels du cinéma fassent des paris amicaux sur le nombre de spectateurs qu'un film attirera à la fin de sa première semaine en salle. 
                Cette pratique, à la fois ludique et ancrée dans les mœurs du secteur, a été le catalyseur de notre projet. Notre objectif est de mettre au point un modèle de machine learning capable de prédire avec la plus grande précision possible le nombre d'entrées qu'un film réalisera. 
                Ce modèle s'appuiera sur des données préalablement collectées, alliant des critères quantitatifs et qualitatifs pour établir ses prévisions.</p>
            </div>
        </div>
        <div id="Objectif" class="tab-content">
            <div class="box">
                <h3>L'objectif du projet :</h3>
                <p>L'objectif central de notre projet est de développer un outil accessible et convivial, permettant à tout utilisateur de prévoir le nombre de spectateurs d'un film à la fin de sa première semaine en salle. 
                En renseignant des paramètres spécifiques de son choix, l'utilisateur pourra obtenir rapidement une estimation précise des entrées en salle.</p>
            </div>
        </div>
        <div id="Streamlit" class="tab-content">
            <div class="box">
                <h3>Pourquoi avoir choisi Streamlit ?</h3>
                <p>Au-delà des fonctionnalités de base de cet applicatif, qui contribuent à rendre nos présentations plus dynamiques et visuellement impactantes, il est important de souligner que le choix de Streamlit pour présenter notre projet a également répondu à plusieurs objectifs pédagogiques. 
                En effet, Streamlit est un outil de plus en plus prisé au sein des entreprises.</p>
                <p>En intégrant Streamlit, nous avons non seulement amélioré l'interactivité et l'impact visuel de notre présentation, mais aussi enrichi notre expérience d'apprentissage avec une application technologique en pleine expansion. 
                Cette démarche nous a permis de nous approprier efficacement cet outil moderne, en vue de l'utiliser plus tard dans nos futures carrières.</p>
            </div>
        </div>
    </div>
</div>

<script>
    function openTab(evt, tabName) {
        var i, tabcontent, tablinks;
        tabcontent = document.getElementsByClassName("tab-content");
        for (i = 0; i < tabcontent.length; i++) {
            tabcontent[i].style.display = "none";
            tabcontent[i].classList.remove("active");
        }
        tablinks = document.getElementsByClassName("tab-link");
        for (i = 0; i < tablinks.length; i++) {
            tablinks[i].className = tablinks[i].className.replace(" active", "");
        }
        document.getElementById(tabName).style.display = "block";
        document.getElementById(tabName).classList.add("active");
        evt.currentTarget.className += " active";
    }
</script>
""", unsafe_allow_html=True)
