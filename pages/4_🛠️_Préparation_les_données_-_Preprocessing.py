import streamlit as st

for i in range(25):
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.subheader("🎥oct23_cda_exploitation-cinématographique🎥")
st.sidebar.markdown("_____________________")
st.sidebar.markdown("Manon FOUQUET")
st.sidebar.markdown("Sylvain BRAIZET")
st.sidebar.markdown("Nicolas DARTOIS")

st.header("🛠️Préparation les données - Preprocessing🛠️")

background_image = '''
    <style>
    .stApp {
        background-color: white;
        background-image: url("https://github.com/NicolasDartois/streamlit_2/blob/main/images/background.jpg?raw=true");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
    }
    .box {
        background-color: white;
        padding: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        box-shadow: 0 10px 12px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        text-align: justify;
    }
    </style>
    '''
st.markdown(background_image, unsafe_allow_html=True)

st.write("### Introduction :")
st.write("Le prétraitement (preprocessing) des données vise à préparer les données brutes pour que notre modèle futur soit le plus performant possible  :")
st.markdown("""
<ul>
    <li>Nettoyant les données en éliminant les valeurs aberrantes (réalisé juste avant la modélisation), et en gérant les valeurs manquantes. NB : le dédoublonnage n'était pas nécessaire.</li>
    <li>Transformant les features en formats compatibles avec les algorithmes d'apprentissage automatique, tels que la normalisation des valeurs et les onehotencoding.</li>
    <li>En améliorant la qualité des données en calculant des scores afin d'optimiser les performances des modèles et de garantir des résultats plus fiables.</li>
</ul>
""", unsafe_allow_html=True)
st.write("### Traitement des valeurs manquantes :")
st.write("Exemple de texte")
st.write("### Formatage des données :")
st.write("Les étapes de formatage des données :")
st.markdown("""
<ul>
    <li>Onehotencoding des genres</li>
    <li>Onehotencoding de l'origine du pays du film (en ayant retenu que 3 catégories : France ou USA ou autre (si France et USA sont en False)</li>
    <li>conversion et reformatage des données budgets : identification de toutes les devises différentes, conversion en euros en utilisant le taux de change à date de chaque devise</li>
    <li>extraction des jours, jours_semaine, mois de la date de sortie des films, puis standardisation cyclique des variables obtenues</li>
    <li>Mise en oeuvre d'un score acteurs, d'un score réalisateurs, d'un score scenaristes, d'un score distributeur</li>
    <li>Description schématique du score Acteurs :</li>
</ul>
<br>
<br>
""", unsafe_allow_html=True)
st.image('images/score_acteur.png')
