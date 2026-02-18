import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CV - Sokhna DIOP",
    page_icon="👩‍🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé corrigé
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 1rem;
}

.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}

h1 {
    color: #1f4e79;
    text-align: center;
    font-size: 3.5rem;
    margin-bottom: 0.5rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

h2 {
    color: #1f4e79;
    border-bottom: 3px solid #1f4e79;
    padding-bottom: 10px;
    font-size: 1.8rem;
}

.card {
    background: linear-gradient(145deg, #ffffff 0%, #f8fafc 100%);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    margin-bottom: 25px;
    border: 1px solid rgba(31,78,121,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}

.sidebar .sidebar-content {
    background: linear-gradient(180deg, #2c5aa0 0%, #1f4e79 100%);
}

.sidebar-title {
    color: white !important;
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.sidebar-text {
    color: #1a1a1a !important;
    font-size: 1rem;
    font-weight: 500;
}

.sidebar-card {
    background: rgba(255,255,255,0.95) !important;
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
    border: 1px solid rgba(31,78,121,0.2);
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR (ANGLAIS) =====
with st.sidebar:
    st.markdown('<div class="sidebar-title">👩‍🎓 Personal Information</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="sidebar-card">
        <h3 style='color: #1f4e79; margin-top: 0; font-size: 1.4rem;'></h3>
        <p class="sidebar-text">📧 diopsokhnasokhnadiop@gmail.com</p>
        <p class="sidebar-text">📍 Dakar, Senegal</p>
    </div>
    """, unsafe_allow_html=True)

# ===== HEADER (UNIQUEMENT NOM EN GRAND) =====
st.markdown("# **SOKHNA DIOP**")

# ===== PROFIL =====
st.markdown('''<div class="card">''', unsafe_allow_html=True)
st.markdown("### 🎯 Profil ")
st.markdown("""
**Étudiante en BTS Géomatique sérieuse et motivée**,  
je possède des compétences solides en **systèmes d'information géographique (SIG)**, **cartographie** et **analyse spatiale**.  
Je maîtrise les outils professionnels comme **ArcGIS** et **QGIS**.  
**Rigoureuse et organisée**, je suis capable de contribuer efficacement à des projets techniques et d'analyse territoriale.
""")
st.markdown('''</div>''', unsafe_allow_html=True)

# ===== EXPERIENCE =====
st.markdown('''<div class="card">''', unsafe_allow_html=True)
st.markdown("### 💼 Expérience Professionnelle")
st.markdown("#### **Projet Académique : Analyse Spatiale**")

st.markdown("""
- **Collecte, traitement et analyse de données géospatiales*
- **Création de bases de données** géospatiales structurées
- **Production de cartes thématiques** professionnelles  
- **Utilisation de QField** pour la collecte de données terrain
- **Systèmes d'Information Géographique (SIG)**
- **Télédétection** et analyse d'images satellites
- **Levées topographiques** et modélisation 3D
""")
st.markdown('''</div>''', unsafe_allow_html=True)

# ===== FORMATION =====
st.markdown('''<div class="card">''', unsafe_allow_html=True)
st.markdown("### 🎓 Formation & Diplômes")

col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("**2026 - En cours**")
with col2:
    st.markdown("**BTS en Géomatique**")
    st.markdown("*CEDT LE G15*")

col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("**2024**")
with col2:
    st.markdown("**Baccalauréat**")
st.markdown('''</div>''', unsafe_allow_html=True)

# ===== COMPÉTENCES =====
st.markdown('''<div class="card">''', unsafe_allow_html=True)
st.markdown("### 🛠 Compétences Techniques & Personnelles")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### **Techniques**")
    tech_skills = [
        "🗺️ **ArcGIS** (Avancé)",
        "🗺️ **QGIS** (Avancé)", 
        "🐍 **Python** (Intermédiaire)",
        "🐘 **PostgreSQL/PostGIS**"
    ]
    for skill in tech_skills:
        st.markdown(skill)

with col2:
    st.markdown("#### **Personnelles**")
    soft_skills = [
        "👥 **Travail en équipe**",
        "📋 **Organisation**",
        "✅ **Rigueur**",
        "🔍 **Esprit d'analyse**",
        "🚀 **Autonomie**"
    ]
    for skill in soft_skills:
        st.markdown(skill)

st.markdown('''</div>''', unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown('''<div style="text-align: center; padding: 2rem; color: #64748b; background: rgba(255,255,255,0.8);">''', unsafe_allow_html=True)
st.markdown("**Disponible immédiatement pour stage ou alternance** 💼")
st.markdown("**Contact : 71-065-31-97** | **Dakar, Sénégal**")
st.markdown('''</div>''', unsafe_allow_html=True)
