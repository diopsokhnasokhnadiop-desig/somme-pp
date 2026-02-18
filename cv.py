import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="CV - Sokhna DIOP",
    page_icon="👩‍🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé amélioré
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
    font-size: 3rem;
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

.stMetric {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 15px;
    color: white;
}

.sidebar .sidebar-content {
    background: linear-gradient(180deg, #1f4e79 0%, #2c5aa0 100%);
}

.sidebar-title {
    color: white !important;
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

.sidebar-text {
    color: #e2e8f0 !important;
    font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR (PERSONAL INFORMATION) - EN ANGLAIS =====
with st.sidebar:
    st.markdown('<div class="sidebar-title">👩‍🎓 Personal Information</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin: 10px 0;'>
        <h3 style='color: white; margin-top: 0;'>Sokhna DIOP</h3>
        <p class="sidebar-text">📧 diopsokhnasokhnadiop@gmail.com</p>
        <p class="sidebar-text">📍 Dakar, Senegal</p>
        <p class="sidebar-text">🎓 BTS Géomatique Student</p>
    </div>
    """, unsafe_allow_html=True)

# ===== HEADER =====
st.markdown("# CURRICULUM VITAE")
st.markdown("**Sokhna DIOP** - Étudiante en BTS Géomatique")

# ===== PROFIL =====
st.markdown('''<div class="card">''', unsafe_allow_html=True)
st.markdown("### 🎯 Profil Professionnel")
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
col1, col2 = st.columns([1, 3])
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
st.markdown('''</div>''', unsafe_allow_html=True)

# ===== FORMATION =====
st.markdown('''<div class="card">''', unsafe_allow_html=True)
st.markdown("### 🎓 Formation & Diplômes")

col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("**2024 - En cours**")
with col2:
    st.markdown("**BTS en Géomatique**")
    st.markdown("*Lycée Technique Industriel de Dakar*")

col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("**2024**")
with col2:
    st.markdown("**Baccalauréat Scientifique**")
    st.markdown("*Mention Bien*")
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
st.markdown('''<div style="text-align: center; padding: 2rem; color: #64748b;">''', unsafe_allow_html=True)
st.markdown("**Disponible immédiatement pour stage ou alternance** 💼")
st.markdown("**Contact : diopsokhnasokhnadiop@gmail.com** | **Dakar, Sénégal**")
st.markdown('''</div>''', unsafe_allow_html=True)
