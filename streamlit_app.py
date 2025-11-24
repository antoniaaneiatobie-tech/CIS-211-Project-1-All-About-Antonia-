import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(
    page_title='Antonia Tobie | Portfolio',
    page_icon='🩷',
    layout='wide'
)

# Custom CSS
st.markdown('''
<style>
    .main-header {font-size: 42px; font-weight: bold; text-align:center;}
    .sub-header {font-size: 24px; text-align:center; color: #666;}
</style>
''', unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title('🧭 Navigation')
page = st.sidebar.radio(
    'Go to',
    ['🏠 Home', '😊 About', '🧳 Projects', '🛠️ Skills', '📝 Resume', '📲 Contact']
)

# -------------------------
# 🏠 Home Page
# -------------------------
if page == '🏠 Home':
    st.markdown('<p class="main-header">Antonia Tobie</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">A 21 Year Old College Student | Medgar Evers College</p>', unsafe_allow_html=True)

    # Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('GPA', '2.5', '📚')
    with col2:
        st.metric('Projects', '1', '💻')
    with col3:
        st.metric('Skills', '5+', '🛠️')

    st.write('---')

    # Intro
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader('Welcome to my safe space! 👋')
        st.write('''
        I am a 21 year old college student majoring in Computer Information Systems and I am learning Python for the first time, HTML, CSS and JavaScript to build innovative solutions.

        🩷 **Current Focus:** Building interactive web applications with Streamlit  
        🎀 **Currently Learning:** Internet and Emerging Technologies (CIS 211)  
        🩵 **Fun Fact:** I love watching Anime and playing video games!
        ''')
    with col2:
        st.image('Tengen.JPG', use_column_width=True)

# -------------------------
# 😊 About Page
# -------------------------
elif page == '😊 About':
    st.title('About Me')

    st.subheader('🗺️ My Journey')
    with st.expander('2025 - Present: Medgar Evers College'):
        st.write('''
        - Major: Computer Information Systems 💻  
        - Relevant Coursework: Internet & Emerging Technologies, Programming, Database Systems, and AI  
        - Activities: Anime Watcher, Tennis Player, and Video Game Lover  
        ''')

    st.subheader('Interests & Hobbies 🎮')
    interests = ['Anime', 'Video Games', 'Cosplaying', 'Tennis', 'Travel', 'Pets']

    cols = st.columns(3)
    for i, interest in enumerate(interests):
        with cols[i % 3]:
            st.info(f'🔷 {interest}')

# -------------------------
# 🧳 Projects Page
# -------------------------
elif page == '🧳 Projects':
    st.title('My Projects')
    st.write('Here are some projects I have worked on:')

    with st.container():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image('https://img2.clipart-library.com/27/tennis-clip-art-images/tennis-clip-art-images-11.jpg')
        with col2:
            st.write('To be honest, I haven’t created many projects yet — but here are some hobbies I enjoy!')

# -------------------------
# 🛠️ Skills Page
# -------------------------
elif page == "🛠️ Skills":
    st.title("My Skills & Strengths")

    st.subheader("My Skills")
    skills_data = {
        "Problem Solving": 85,
        "Critical Thinking": 75,
        "Creativity": 100,
        "Active Listening": 95,
        "Collaboration": 100
    }

    for skill, level in skills_data.items():
        col1, col2 = st.columns([1,5])
    
        with col1:
          st.write(skill)
        with col2:
          st.progress(level/100)
    
          st.subheader('Tools & Technologies')
    
          col1, col2, col3, col4, col5, = st.columns(5)
          with col1:
            st.success('Problem solving')
            st.info('Fixing Problems')
            st.warning('Takes a few tries')
    
          with col2:
            st.success('Critical thinking')
            st.info('Thinking deeper')
            st.warning('may take a while')
        
          with col3:
            st.success('Creativity')
            st.info('coming up with new things')
            st.warning('Creativity takes patience')
     
          with col4:
            st.success('Active listening')
            st.info('I like listening to new ideas')
            st.warning('Shows interest in new things')
     
          with col5:
            st.success('Collaboration')
            st.info('Working with others')
            st.warning('Teamwork')



elif page == "📝 Resume":
    st.title('Resume')
    # Read PDF from my GitHub repository
    with open('Antonia Tobie resume.pdf', 'rb') as pdf_file:
        PDFbyte = pdf_file.read()
        
        st.download_button(
        label ='🔻 Download Full Resume (PDF)',
        data = PDFbyte,
        file_name = 'Antonia Tobie resume.pdf',
        mime ='application/pdf'
        )

elif page == '📩 Contact':
    st.title("Let's Connect!")
    
    col1, = st.columns(1)
    
    with col1:
        st.subheader('Send me a message.')
        
        st.write('''
            📧 **Email:** Antonia.aneia.tobie@gmail.com
        
            👩‍💻 **Github:** [https://github.com/antoniaaneiatobie-tech](https://github.com)
        
            📷 **Instagram:** [@savagekitty](https://instagram.com)
        
        ''')
        
        # Fun interative element
        st.subheader('Current Status')
        
        status = st.selectbox(
            "I'm currently:",
            [
                '👩‍💻 Coding',
                '📕 Studying',
                '🍕 Eating food',
                '🎮 Gaming',
                '😴 Sleeping'
            ]
        )
        
        
        st.info(f'Status: {status}')
    
    # Footer
    st.write('---')
    st.markdown(
        f'<center>Made with 💗 using Streamlit | © {datetime.now().2025} Antonia Tobie </center>',
        unsafe_allow_html = True
    )



   
