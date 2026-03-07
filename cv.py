import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CV - Sokhna DIOP",
    page_icon="👩‍🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS amélioré
st.markdown("""
<style>

.main {
    background: linear-gradient(135deg,#f5f7fa,#c3cfe2);
}

.block-container{
    padding-top:2rem;
    max-width:1200px;
}

h1{
    color:#1f4e79;
    text-align:center;
    font-size:3.5rem;
}

h2{
    color:#1f4e79;
    border-bottom:3px solid #1f4e79;
}

.card{
    background:white;
    padding:30px;
    border-radius:20px;
    box-shadow:0 10px 25px rgba(0,0,0,0.15);
    margin-bottom:25px;
}

/* SIDEBAR */

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#2c5aa0,#1f4e79);
}

.sidebar-card{
    background:white;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
}

.sidebar-name{
    font-size:22px;
    font-weight:bold;
    color:#1f4e79;
    text-align:center;
}

.sidebar-text{
    font-size:14px;
    color:#333;
}

.sidebar-section{
    background:white;
    padding:15px;
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
        <div class="sidebar-text"> diopsokhnasokhnadiop@gmail.com</div>
        <div class="sidebar-text"> Dakar, Sénégal</div>
    </div>
    """, unsafe_allow_html=True)

    # Disponibilité
    st.markdown("""
    <div class="sidebar-section">
    <h4 style="color:#1f4e79;">📅 Disponibilité</h4>

    ✔ Disponible pour stage  
    ✔ Disponible pour projets SIG  
    ✔ Disponible pour collecte de données terrain  

    </div>
    """, unsafe_allow_html=True)

# ===== HEADER =====

st.markdown("# **Etudiante en Geomatique**")

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

st.markdown("#### **Projet Académique : Analyse Spatiale**")

col1, col2 = st.columns([1,3])

with col1:
    st.markdown("**2024 - En cours**")

with col2:
    st.markdown("*Collecte, traitement et analyse de données géospatiales*")

st.markdown("""
- **Création de bases de données** géospatiales structurées
- **Production de cartes thématiques** professionnelles  
- **Utilisation de QField** pour la collecte de données terrain
- **Systèmes d'Information Géographique (SIG)**
- **Télédétection** et analyse d'images satellites
- **Levées topographiques** et modélisation 3D
""")

st.markdown('</div>', unsafe_allow_html=True)

# ===== FORMATION =====

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### Diplômes")

st.markdown("**BTS en Géomatique**")

st.markdown("**Baccalauréat**")

st.markdown('</div>', unsafe_allow_html=True)

# ===== COMPÉTENCES =====

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("### Compétences Techniques & Personnelles")

col1, col2 = st.columns(2)

with col1:

    st.markdown("#### Techniques")

    tech_skills=[
        "🗺️ **ArcGIS** (Avancé)",
        "🗺️ **QGIS** (Avancé)",
        "🐍 **Python** (Intermédiaire)",
        "🐘 **PostgreSQL/PostGIS**"
    ]

    for skill in tech_skills:
        st.markdown(skill)

with col2:

    st.markdown("#### Personnelles")

    soft_skills=[
        "Travail en équipe",
        "Organisation",
        "Rigueur",
        "Esprit d'analyse",
        "Autonomie"
    ]

    for skill in soft_skills:
        st.markdown(skill)

st.markdown('</div>', unsafe_allow_html=True)

# ===== FOOTER =====


</div>
""", unsafe_allow_html=True)
