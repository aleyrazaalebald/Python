import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NFL Football Stats (Rushing) Explorer')

st.markdown(""" 
This app performs simple webscraping of NFL Fooball player stats.
""")

st.sidebar.header('User Input Features')

selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990, 2020))))
# Web Scraping of NFL player stats
# https://www.pro-football-reference.com/years/2019/rushing.htm
@st.cache_data
def load_data(year):
    url = "https://www.pro-football-reference.com/years/" + str(year) + "/rushing.htm"
    html = pd.read_html(url, header = 1)  # main Webscraping a site
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk'], axis=1)
    return playerstats
playerstats = load_data(selected_year)

# Sidebar - Team Selection
sorted_unique_team = sorted(playerstats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)
selected_team = st.sidebar.multselect('Team', sorted_unique_team, sorted_unique_team)
# Sidebar - Position Selection
unique_pos = ['RB', 'QB', 'WR', 'FB', 'TE']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)

# Filtering data
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos))]
st.header('Display Player Stats of SelectedTeam(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' column')

# Download NBA Player stats data
def filedownloa(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode() # strings <-> bytes
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CV File</a>'
    return href

# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorreltion Matrix Heatmap')
    df_selected_team.to_cv('output.csv',inex=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indice_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()
