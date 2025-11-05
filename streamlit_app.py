import streamlit as st

import pandas as pd
from datetime import datetime

# page Config
st.set_page_config(
  page_title = 'Antonia Tobie | Portfolio',
  page_icon='🩷',
  layout = 'wide'
)

# Custom CSS (optional - for styling)
st.markdown('''
                <style>
                    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                    .sub-header {font-size: 24px; text-align:center; color: #666;}
                </style>
            ''', unsafe_allow_html = True)


# Sidebar
st.sidebar.title('🧭 Navigation')
page = st.sidebar.radio('Go to',
                        ['🏠 Home', '😊 About', '🧳 Projects', '🛠️ Skills', '📝 Resume', '📲 Contact'])

 
# Home
if page == '🏠 Home':
    st.markdown('<p class="main-header">Antonia Tobie</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">A 21 Year Old College Student | Medgar Evers College</p>', unsafe_allow_html=True)

# Three columns for stats
col1, col2, col3 = st.columns (3)

with col1:
  st.metric('GPA', '2.5', '📚')
with col2:
  st.metric('Projects', '1', '💻')
with col3:
  st.metric('skills', '5+', '🛠️')

st.write('---')


# Introduction with columns
col1, col2 = st.columns([2,1])
with col1: 
  st.subheader('Welcome to my safe space! 👋')
  st.write('''
             I am a 21 year old college student majoring in Computer Information Systems and I am learning Python for the first time, HTML, CSS and JavaScript to build innovative solutions.

            🩷 **Current Focus:** Building interactive web applications with Streamlit

            🎀 **Currently Learning:** Internet and Emergin Technologies (CIS 211)

            🩵 **Fun Fact:** I love watching Anime and playing video games!
            ''')
with col2:
  # Placeholder for image
   st.image(' Tengen .JPG', use_column_width=True)


# About page
elif page == '😊 About':
 st.title('About Me')


# Timeline of my CIS Journey
st.subheader('🗺️ My Journey')
with st.expander('2025 - Present: Medgar Evers College'):
  st.write('''
          - Major: Computer Information Systems 💻
          - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems and AI
          - Activities: Anime Watcher, Tennis Player and Video game lover
          ''')
  with st.expander('')
  
