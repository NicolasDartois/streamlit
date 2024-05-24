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

from bokeh.plotting import figure, output_file, save
from bokeh.embed import file_html
from bokeh.resources import CDN
from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.transform import cumsum
from math import pi

from include.css_and_credit import css_and_credit

st.set_page_config(page_title="Exploitation cinématographique", page_icon='🎬', layout="wide")

css_and_credit()

st.header("📊Analyse des Données (DataViz)📊")

st.markdown("<br><br><br>", unsafe_allow_html=True)
allocine = pd.read_csv('data/allocine.csv')
allocine_budget = pd.read_csv('data/Allocine_v2_8.csv')

pays_counts = allocine['pays'].value_counts()
top_pays = pays_counts[:8]
autres = pays_counts[8:].sum()
top_pays['Autres'] = autres  

data = pd.Series(top_pays).reset_index(name='value').rename(columns={'index':'pays'})
data['angle'] = data['value']/data['value'].sum() * 2*pi
data['color'] = ['#f6a580', '#92c5de', '#0571b0', '#ca0020', '#f4a582', '#92c5de', '#0571b0', '#d4b9da']

p = figure(plot_height=350, title="Répartition des films par pays", toolbar_location=None,
           tools="hover", tooltips="@pays: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4, 
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='pays', source=ColumnDataSource(data))

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

bokeh_plot_html = file_html(p, CDN, "my_plot")

markdown_content = f"""
<div class="box">
    {bokeh_plot_html}
</div>
"""

st.markdown(markdown_content, unsafe_allow_html=True)


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
            fig2 = px.scatter(
                        allocine, 
                        x='cumul_france', 
                        y='premiere_semaine_france',
                        hover_data=['titre_original'],
                        title=f'📈 Corrélation entre le cumul en France et la première semaine en France: 0.92',
                        labels={'cumul_france': 'Cumul en France', 'premiere_semaine_france': 'Première semaine en France'},
                        opacity=0.5,
                        trendline='ols'
                        )
            fig2.data[1].line.color = 'red'
            fig2.update_layout(margin={'l': 40, 'b': 40, 't': 80, 'r': 40}, hovermode='closest')
            fig2.update_xaxes(showgrid=True, title='Cumul en France')
            fig2.update_yaxes(showgrid=True, title='Première semaine en France')
            st.plotly_chart(fig2)
            
            st.markdown('<div class="box"><p>En calculant la corrélation entre la première semaine et le cumul en France, on obtient un score de 0.92. La corrélation est donc positive et très élevée. Ainsi, si un film réalise de bonnes performances en première semaine en termes d’entrées, il a des chances de connaître le succès pendant toute son exploitation cinématographique. Cela suppose donc que le nombre d’entrées de la première semaine peuvent être utilisées pour estimer le nombre total d’entrées.</p></div>', unsafe_allow_html=True)

#---------------#
col1, col2, col3, col4, col5 = st.columns([2, 8, 1, 8, 2])

with col2: 
            fig3 = px.box(allocine, x="premiere_semaine_france",
                        hover_data=['titre_original'],
                        title='🎫 Analyse de la distribution de notre target: première semaine en France',
                        labels={'premiere_semaine_france': 'Première semaine en France'})
            fig3.update_layout(width=750, height=400)
            fig3.update_layout(xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgrey'))
            st.plotly_chart(fig3)
            
            st.markdown('<div class="box"><p>Ces données suggèrent une forte asymétrie dans la distribution des performances des films. La présence de quelques films avec des résultats exceptionnels lors de la première semaine indique que ces films peuvent être des moteurs significatifs pour l’industrie, tandis que la majorité des films affichent des performances beaucoup plus modestes.</p></div>', unsafe_allow_html=True)

with col4:
            fig4 = px.scatter(
                        allocine_budget, 
                        x='budget_euro', 
                        y='premiere_semaine_france',
                        hover_data=['titre_original'],
                        title='📈 Corrélation entre le budget du film et la première semaine en France. Pearson : 0.62',
                        labels={'budget_euro': 'Budget', 'premiere_semaine_france': 'Première semaine en France'},
                        opacity=0.5,
                        trendline='ols'
                        )
            fig4.data[1].line.color = 'red'
            fig4.update_layout(margin={'l': 40, 'b': 40, 't': 80, 'r': 40}, hovermode='closest')
            fig4.update_xaxes(showgrid=True, title='Budget')
            fig4.update_yaxes(showgrid=True, title='Première semaine en France')
            st.plotly_chart(fig4)

            st.markdown('<div class="box"><p>Ces graphiques illustrent la corrélation entre le budget d’un film et le nombre d’entrées en première semaine en France. On remarque une corrélation positive avec un coefficient de Pearson de 0,62.</p></div>', unsafe_allow_html=True)

