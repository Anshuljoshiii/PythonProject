import pandas as pd
#import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide", page_title="India Census 2011 Data Visualization",page_icon="📊")

df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('India Census 2011 Data Visualization')
selected_state = st.sidebar.selectbox('select a state',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')
if plot:
    st.text("Size Represent Primary Parameter")
    st.text("Color Represent Secondary Parameter")
    if selected_state == 'Overall India':
        fig=px.scatter_mapbox(df,lat="Latitude",lon="Longitude",size=primary,color=secondary,zoom=4,size_max=35,
                              hover_name="District", mapbox_style='carto-positron',width=1200,height=700)
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6, size_max=35,
                                hover_name="District", mapbox_style='carto-positron', width=1200, height=700)
        st.plotly_chart(fig,use_container_width=True)


