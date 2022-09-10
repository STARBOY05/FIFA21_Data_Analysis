import pandas as pd
import streamlit as st
import helper
import requests
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("FIFA21_players.csv")
flagData = requests.get('https://flagcdn.com/en/codes.json').json()
st.sidebar.image('https://images.launchbox-app.com/d15edafa-33ce-4621-8076-1345829d0ef0.png')
st.sidebar.title('FIFA 2021 ANALYSIS')

playerNames = data['PlayerName'].sort_values()

selected_option = st.sidebar.radio(
    "Overall Analysis",
    ('Overall Performance', 'Specific Player Statistics'))


if selected_option == 'Overall Performance':
    st.header('Fastest Players in FIFA 2021')
    st.table(data[["Acceleration","PlayerName","BestPositions",'Age','Nationality','SprintSpeed']].nlargest(10, ['Acceleration']).set_index('PlayerName').head(10))
    st.header('Tallest Players in FIFA 2021')
    st.table(data[['PlayerHeight','PlayerName','PlayerWeight','BestPositions','Age','Nationality']].nlargest(10, ['PlayerHeight']).set_index('PlayerName').head(10))
    st.header('Best Defenders in FIFA 2021')
    st.table(data[["DefensiveAwareness","PlayerName","StandingTackle", "SlidingTackle",'Age','Nationality']].nlargest(10, ['DefensiveAwareness']).set_index('PlayerName').head(10))
    st.header('Best Players with Long Passes in FIFA 2021')
    st.table(data[["LongPassing",'ShortPassing',"PlayerName","BestPositions",'Age','Nationality']].nlargest(10, ['LongPassing']).set_index('PlayerName').head(10))
    st.header('Best Players with ShortPasses in FIFA 2021')
    st.table(data[["LongPassing",'ShortPassing',"PlayerName","BestPositions",'Age','Nationality']].nlargest(10, ['ShortPassing']).set_index('PlayerName').head(10))
    st.header('Best GoalKeepers by Reflex in FIFA 2021')
    st.table(data[["Reflexes","PlayerName","Kicking","Handling",'Age','Nationality']].nlargest(10, ['Reflexes']).set_index('PlayerName').head(10))
    preferred_foot_labels = data["PreferredFoot"].value_counts().index # (Right,Left) 
    preferred_foot_values = data["PreferredFoot"].value_counts().values # (Right Values, Left Values)
    st.header("Player's Preferred Foot")
    fig = go.Figure(data=[go.Pie(labels=preferred_foot_labels, values=preferred_foot_values, textinfo='label+percent',
                                insidetextorientation='radial'
                            )])
    st.plotly_chart(fig)
if selected_option == 'Specific Player Statistics':
    selected_player = st.sidebar.selectbox(
        "Who's your favourite player",
        (playerNames))
    playerData = helper.getPlayer(data, selected_player)
    nationFlag = helper.getNationalityFlag(flagData, playerData['Nationality'].values[0])
    col1, col2 = st.columns([5, 1])
    with col1:
        st.title(playerData['PlayerName'].values[0])
    with col2:
        st.image('https://flagcdn.com/96x72/' + nationFlag + '.png')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('Height')
        st.subheader(playerData['PlayerHeight'].values[0])
    with col2:
        st.header('Weight')
        st.subheader(playerData['PlayerWeight'].values[0])
    with col3:
        st.header('Best Positions')
        st.subheader(playerData['BestPositions'].values[0])
    with col1:
        st.header('Overall Rating')
        st.subheader(playerData['BestOverallRating'].values[0])
    with col2:
        st.header('Wage')
        st.subheader(playerData['Wage'].values[0])
    with col3:
        st.header('Sprint Speed')
        st.subheader(playerData['SprintSpeed'].values[0])
    with col1:
        st.header('Nationality')
        st.subheader(playerData['Nationality'].values[0])
    with col2:
        st.header('Ball Control')
        st.subheader(playerData['BallControl'].values[0])
    with col3:
        st.header('Agility')
        st.subheader(playerData['Agility'].values[0])
    
