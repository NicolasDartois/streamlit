import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.io import to_html
from bokeh.plotting import figure
from bokeh.models import HoverTool
from include.css_and_credit import css_and_credit

st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()

col1, col2, col3 = st.columns([3, 3, 3])
with col2:
            st.header("📊Analyse des Données (DataViz)📊")

st.markdown("<br><br><br>", unsafe_allow_html=True)
allocine = pd.read_csv('data/allocine.csv')

#---------------#
col1, col2, col3, col4, col5 = st.columns([2, 8, 1, 8, 2])

with col2:            
            pays_counts = allocine['pays'].value_counts()
            top_pays = pays_counts[:8]
            autres = pays_counts[8:].sum()
            top_pays['Autres'] = autres    
            fig1 = go.Figure(data=[go.Pie(labels=top_pays.index, values=top_pays.values, hole=.3)])
            fig1.update_traces(textposition='inside', textinfo='percent+label')
            fig1.update_layout(
                        title_text='🌎 Répartition des films par pays',
                        annotations=[dict(text='Pays', x=0.5, y=0.5, font_size=20, showarrow=False)],
                        legend_title="Pays"
                        )
            st.plotly_chart(fig1)
            
            st.markdown('<div class="box"><p>La France (38,9%) et les U.S.A (30,7%) se partagent une importante part du marché cinématographique français. On remarque l’incroyable exportabilité des films américains qui égalise presque le volume de films produits par le pays d’où sont issues les données.</p></div>', unsafe_allow_html=True)

with col4:
            fig4 = px.scatter(
                        allocine, 
                        x='cumul_france', 
                        y='premiere_semaine_france',
                        hover_data=['titre_original'],
                        title=f'📈 Corrélation entre le cumul en France et la première semaine en France: 0.92',
                        labels={'cumul_france': 'Cumul en France', 'premiere_semaine_france': 'Première semaine en France'},
                        opacity=0.5,
                        trendline='ols'
                        )
            fig4.data[1].line.color = 'red'
            fig4.update_layout(margin={'l': 40, 'b': 40, 't': 80, 'r': 40}, hovermode='closest')
            fig4.update_xaxes(showgrid=True, title='Cumul en France')
            fig4.update_yaxes(showgrid=True, title='Première semaine en France')
            st.plotly_chart(fig4)
            
            st.markdown('<div class="box"><p>En calculant la corrélation entre la première semaine et le cumul en France, on obtient un score de 0.92. La corrélation est donc positive et très élevée. Ainsi, si un film réalise de bonnes performances en première semaine en termes d’entrées, il a des chances de connaître le succès pendant toute son exploitation cinématographique. Cela suppose donc que le nombre d’entrées de la première semaine peuvent être utilisées pour estimer le nombre total d’entrées.</p></div>', unsafe_allow_html=True)

#---------------#
col1, col2, col3, col4, col5 = st.columns([2, 8, 1, 8, 2])

with col2: 
            fig2 = px.box(allocine, x="premiere_semaine_france",
                        hover_data=['titre_original'],
                        title='🎫 Analyse de la distribution de notre target: première semaine en France',
                        labels={'premiere_semaine_france': 'Première semaine en France'})
            fig2.update_layout(width=750, height=400)
            fig2.update_layout(xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgrey'))
            st.plotly_chart(fig2)
            
            st.markdown('<div class="box"><p>Ces données suggèrent une forte asymétrie dans la distribution des performances des films. La présence de quelques films avec des résultats exceptionnels lors de la première semaine indique que ces films peuvent être des moteurs significatifs pour l’industrie, tandis que la majorité des films affichent des performances beaucoup plus modestes.</p></div>', unsafe_allow_html=True)

with col4:
            allocine_budget = pd.read_csv('data/Allocine_v2_8.csv')
            correlation = allocine_budget['premiere_semaine_france'].corr(allocine_budget['budget_euro'])
            
            def millions_formatter(x, pos):
                return f'{x / 1e6}M'
            formatter = FuncFormatter(millions_formatter)
            
            plt.figure(figsize=(20, 10))
            
            sns.regplot(x='budget_euro', y='premiere_semaine_france', data=allocine_budget)
            plt.xlabel('Budget du film')
            plt.ylabel('Première semaine en France (nombre de spectateurs)')
            plt.title(f'Corrélation entre le budget du film et la première semaine en France. Pearson : 0.62')
            plt.gca().yaxis.set_major_formatter(formatter)
            plt.gca().xaxis.set_major_formatter(formatter)
            st.pyplot(plt)
            
            st.markdown('<div class="box"><p>Ces graphiques illustrent la corrélation entre le budget d’un film et le nombre d’entrées en première semaine en France. On remarque une corrélation positive avec un coefficient de Pearson de 0,62.</p></div>', unsafe_allow_html=True)

