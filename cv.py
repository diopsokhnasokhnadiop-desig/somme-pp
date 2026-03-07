import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CV - Sokhna DIOP",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===== STYLE CSS =====

st.markdown("""
<style>

.main {
    background: linear-gradient(120deg,#eef2f7,#d9e2ec);
}

.block-container{
    padding-top:2rem;
    max-width:1100px;
}

/* TITRE */

h1{
    color:#1f3c5a;
    text-align:center;
    font-size:3rem;
    margin-bottom:30px;
}

/* TITRES */

h2, h3{
    color:#1f3c5a;
    border-bottom:2px solid #d0d7de;
    padding-bottom:6px;
}

/* CARDS */

.card{
    background:white;
    padding:35px;
    border-radius:18px;
    box-shadow:0 6px 20px rgba(0,0,0,0.08);
    margin-bottom:25px;
    transition:0.3s;
}

.card:hover{
    box-shadow:0 10px 30px rgba(0,0,0,0.15);
    transform:translateY(-3px);
}

/* SIDEBAR */

[data-testid="stSidebar"]{
    background:#1f3c5a;
}

.sidebar-card{
    background:white;
    padding:22px;
    border-radius:14px;
    margin-bottom:20px;
}

.sidebar-name{
    font-size:22px;
    font-weight:600;
    color:#1f3c5a;
    text-align:center;
}

.sidebar-text{
    font-size:14px;
    color:#444;
}

.sidebar-section{
    background:white;
    padding:18px;
    border-radius:12px;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====

with st.sidebar:

    st.markdown("""
    <div class="sidebar-card">
        <div class="sidebar-name">Sokhna DIOP</div>
        <br>
        <div class="sidebar-text">Email : diopsokhnasokhnadiop@gmail.com</div>
        <div class="sidebar-text">Localisation : Dakar, Sénégal</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-section">

    <h4>Disponibilité</h4>

    Disponible pour stage  
    Disponible pour projets SIG  
    Disponible pour collecte de données terrain  

    </div>
    """, unsafe_allow_html=True)

# ===== HEADER =====

st.markdown("# Sokhna DIOP")
st.markdown("### Étudiante en Géomatique")

# ===== PROFIL =====

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### Profil")

st.markdown("""
Géomaticienne spécialisée en systèmes d'information géographique (SIG), cartographie numérique et analyse spatiale. 
Maîtrise les logiciels professionnels ArcGIS et QGIS pour produire des cartes précises et des analyses territoriales. 
Participe activement à des projets techniques d'envergure.
""")

st.markdown('</div>', unsafe_allow_html=True)

# ===== EXPERIENCE =====

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### Expérience Professionnelle")

st.markdown("Projet Académique : Analyse Spatiale")

col1, col2 = st.columns([1,3])

with col1:
    st.markdown("2024 - En cours")

with col2:
    st.markdown("Collecte, traitement et analyse de données géospatiales")

st.markdown("""

Création de bases de données géospatiales structurées  

Production de cartes thématiques professionnelles  

Utilisation de QField pour la collecte de données terrain  

Systèmes d'Information Géographique (SIG)

Télédétection et analyse d'images satellites

Levées topographiques et modélisation 3D

""")

st.markdown('</div>', unsafe_allow_html=True)

# ===== FORMATION =====

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### Diplômes")

st.markdown("BTS en Géomatique")

st.markdown("Baccalauréat")

st.markdown('</div>', unsafe_allow_html=True)

# ===== COMPÉTENCES =====

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### Compétences Techniques et Personnelles")

col1, col2 = st.columns(2)

with col1:

    st.markdown("#### Techniques")

    st.markdown("""
ArcGIS (Avancé)

QGIS (Avancé)

Python (Intermédiaire)

PostgreSQL / PostGIS
""")

with col2:

    st.markdown("#### Personnelles")

    st.markdown("""
Travail en équipe

Organisation

Rigueur

Esprit d'analyse

Autonomie
""")

st.markdown('</div>', unsafe_allow_html=True)
