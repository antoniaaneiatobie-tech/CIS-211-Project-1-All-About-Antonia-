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
    st.subheader('Interests & Hobbies 🏀')
  interests = ['Anime', 'Video games', 'Cosplaying', 'Tennis', 'Travel', 'Pets']

  # Display the interests in columns
  cols = st.columns(3)
  for i, interest in enumerate(interests):
    with cols[i % 3]:
      st.info(f'🔷 {interest}')

  elif page == '🧳 Projects':
  st.title('My Projects')
 elif page == '😊 About':
    st.title('About Me')

    # Timeline of my CIS Journey
    st.subheader('🗺️ My Journey')
    with st.expander('2025 - Present: Medgar Evers College'):
        st.write('''
        - Major: Computer Information Systems 💻
        - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, and AI
        - Activities: Anime Watcher, Tennis Player, and Video Game Lover
        ''')
        
        st.subheader('Interests & Hobbies 🎮')
        interests = ['Anime', 'Video games', 'Cosplaying', 'Tennis', 'Travel', 'Pets']

        # Display the interests in columns
        cols = st.columns(3)
        for i, interest in enumerate(interests):
            with cols[i % 3]:
                st.info(f'🔷 {interest}')


elif page == '🧳 Projects':
    st.title('My Projects')
    st.write('Here are some projects I have worked on:')

    # Project 1
    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://img2.clipart-library.com/27/tennis-clip-art-images/tennis-clip-art-images-11.jpg')  
        with col2:
            st.write('To be completely honest i haven't really worked on any but here are some pictures of my hobbies!')
 st.write('Here are some projects I have worked on:')
  # Project 1
    with st.container():
    col1, col2 = st.columns([1, 2])
  
        with col1:
        st.image('https://static.wikia.nocookie.net/voicelines/images/6/60/V3_Junko_Enoshima_Cosplay.png/revision/latest?cb=20210108191916')

  elif page == '🛠 Skills':
  st.title('Technical Skills')

  # Skills with progress bars
  st.subheader('Programming Languages')

  skills_data = {
    'Python' : 85,
    'HTML/CSS' : 70,
    'JavaScript' : 60,
    'SQL' : 50,
    'Technical Writing' : 40
  }

  for skill, level in skills_data.items():
    col1, col2 = st.columns([1,3])
    with col1:
      st.write(skill)
    with col2:
      st.progress(level/100)

  st.subheader('Tools & Technologies')

  col1, col2, col3 = st.columns(3)
  with col1:
    st.success('Excel')
    st.info('Word')
    st.warning('Access')

  with col2:
    st.success('PowerPoint')
    st.info('Google Docs')
    st.warning('ChatGPT/AI Tools')
    
  with col3:
    st.success('Presentations')
    st.info('Writing')
    st.warning('Social Media')
    
        

