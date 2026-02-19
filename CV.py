import streamlit as st

# Configuration de la page
st.set_page_config(page_title="CV - Léontine Tendeng", layout="centered")

# Titre
st.title("📄 Curriculum Vitae")
st.header("Léontine Théodoria Élisabeth Tendeng")

# Informations personnelles
st.subheader("👤 Informations personnelles")
st.write("📍 Adresse : Dakar, Sénégal")
st.write("📞 Téléphone : 78 128 11 19")
st.write("✉️ Email : leontinetendeng46@email.com")
st.write("🌍 Nationalité : Sénégalaise")

# Profil
st.subheader("🎯 Profil")
st.write("""
Étudiante en BTS Géomatique (2ᵉ année) et en Administration Économique et Sociale (AES) à l’Université Virtuelle du Sénégal (UVS).
Je possède des compétences en cartographie, SIG, analyse spatiale et bases de données.
Motivée, organisée et rigoureuse, je souhaite contribuer à des projets liés à la gestion territoriale et au développement.
""")

# Formation
st.subheader("🎓 Formation")
st.write("2024 – 2026 : BTS Géomatique (2ᵉ année)")
st.write("Institut de formation en géomatique – CEDT G15 Dakar")

st.write("2025 – 2026 : Licence 1 Administration Économique et Sociale (AES)")
st.write("Université Virtuelle du Sénégal (UVS)")

st.write("2024 : Baccalauréat")
st.write("Série : L")

# Compétences
st.subheader("🧠 Compétences")

st.markdown("""
- SIG : ArcGIS, QGIS  
- Cartographie numérique  
- Géoréférencement et numérisation  
- Bases de données spatiales  
- Analyse territoriale  
- Microsoft Office (Word, Excel, PowerPoint)  
""")

# Expériences académiques
st.subheader("💼 Expériences académiques")
st.write("Projet cartographique – Réseau routier urbain")
st.write("Collecte de données, numérisation et production de cartes thématiques sous ArcGIS.")

st.write("Projet SIG – Mobilité urbaine")
st.write("Analyse spatiale des déplacements et cartographie des zones de congestion.")

# Langues
st.subheader("🌐 Langues")
st.write("Français : Courant")
st.write("Wolof : Courant")
st.write("Anglais : Niveau lycee")

# Centres d’intérêt
st.subheader("⭐️ Centres d’intérêt")
st.write("- Aménagement du territoire")
st.write("- Teledetection")
st.write("- Technologies géospatiales")
st.write("- Topographie")
st.write("- Cartographie")