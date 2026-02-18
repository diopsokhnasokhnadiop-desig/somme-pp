import streamlit as st

st.set_page_config(page_title="Demande de Stage", page_icon="📄", layout="wide")

# ===== STYLE CSS =====
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 2rem;
}

h1 {
    color: #1f4e79;
    text-align: center;
}

h2 {
    color: #1f4e79;
    border-bottom: 2px solid #1f4e79;
    padding-bottom: 5px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR (INFOS PERSONNELLES) =====
st.sidebar.title("👩‍🎓 Informations")

st.sidebar.markdown("### Sokhna DIOP")
st.sidebar.write("📧 diopsokhnasokhnadiop@gmail.com")
st.sidebar.write("📍 Dakar")

# ===== HEADER =====
st.title("CURRICULUM VITAE")
st.markdown('</div>', unsafe_allow_html=True)

# ===== OBJECTIF =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🎯 Profil")

st.write("""
Étudiante en BTS géomatique,sérieuse et motivée, 
je possède des compétences en systèmes d'information géographique (SIG), cartographie et analyse spatiale.
Je maitrise des outils comme ArcGIS et QGIS. 
Rigoureuse et organisée, je suis capable de contribuer efficacement a des projet techniques et d'analyse 
territoriale.
""")

# ===== FORMATION =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🎓 Formation et Diplôme")

st.write("**Baccalauréat** — 2024 (Série Scientifique)")
st.write("**BTS en Géomatique / SIG** — En cours")
st.write("• Systèmes d’Information Géographique")
st.write("• Cartographie")
st.write("• Télédétection")
st.write("• Base de données")

st.markdown('</div>', unsafe_allow_html=True)

# ===== EXPERIENCE =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("💼 Expérience")

st.write("**Projet académique : Analyse spatiale**")
st.write("• Création de base de données")
st.write("• Production de cartes thématiques")
st.write("• Utilisation de QGIS et ArcGIS")

st.markdown('</div>', unsafe_allow_html=True)

# ===== COMPETENCES =====
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header("🛠 Compétences")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Techniques")
    st.write("ArcGIS")
    st.write("QGIS")
    st.write("Python")
    st.write("PostgreSQL")

with col2:
    st.subheader("Personnelles")
    st.write("Travail en équipe")
    st.write("Organisation")
    st.write("Rigueur")
    st.write("Esprit d’analyse")

st.markdown('</div>', unsafe_allow_html=True)
