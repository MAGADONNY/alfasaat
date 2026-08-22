import streamlit as st

# 1. Podešavanje stranice (Uvek na samom vrhu)
st.set_page_config(
    page_title="ALFASAAT MEDIA DOO",
    page_icon="☀️",
    layout="wide"
)

# 2. Python trik za garantovanu sivu boju kartica i beli okvir
st.markdown(
    """
    <style>
    div[data-testid="stVerticalBlock"] > div:has(div[data-testid="element-container"]) {
        background-color: #2D3139 !important;
        border: 2px solid #FFFFFF !important;
        border-radius: 12px !important;
        padding: 25px !important;
        margin-bottom: 15px !important;
    }
    /* Sprečava da se glavna sekcija i slika uokvire */
    div[data-testid="stColumn"] > div {
        background-color: transparent !important;
        border: none !important;
        padding: 0px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. GLAVNA SEKCIJA: Vaš tekst i nova slika sa logoom
kolona_naslov, kolona_slika = st.columns(2, vertical_alignment="center")

with kolona_naslov:
    st.title("ALFASAAT MEDIA DOO")
    st.subheader("Vaš partner za energetsku efikasnost i maksimalnu bezbednost")
    st.write(
        """
        Prelazak na solarnu energiju nikada nije bio lakši. Projektujemo i ugrađujemo 
        solarne sisteme vrhunskog kvaliteta i obezbeđujemo vaš prostor najmodernijim 
        video nadzorom i alarmima.
        """
    )
    st.button("Saznajte više o nama", key="hero_saznaj_vise")

with kolona_slika:
    try:
        st.image("solarni_paneli.jpg", use_container_width=True)
    except:
        st.info("Prikažite vašu novu sliku ovde.")

st.divider()

# 4. SEKCIJA: Tri glavna box-a (Usluge)
st.header("⚡ Naše ključne oblasti poslovanja")
st.write("") 

# Kreiramo 3 kolone za tri odvojena box-a
box1, box2, box3 = st.columns(3)

# Prvi box: SOLARNI PANELI
with box1:
    st.subheader("☀️ SOLARNI PANELI")
    st.write(
        """
        Kompletna rešenja za energetsku nezavisnost. Projektovanje, 
        montaža i održavanje solarnih elektrana za kuće i firme.
        """
    )
    st.write("**• Smanjenje računa**")
    st.write("**• Zelena energija**")
    st.write("**• Vrhunska oprema**")

# Drugi box: ALARMI
with box2:
    st.subheader("🚨 ALARMI")
    st.write(
        """
        Najmoderniji protivprovalni sistemi i pametni alarmni uređaji 
        koji trenutno javljaju svaku opasnost direktno na vaš telefon.
        """
    )
    st.write("**• Dojava na mobilni**")
    st.write("**• Senzori pokreta**")
    st.write("**• 24/7 Zaštita**")

# Treći box: VIDEO NADZOR
with box3:
    st.subheader("📹 VIDEO NADZOR")
    st.write(
        """
        Profesionalne kamere visoke rezolucije sa pametnom analitikom, 
        prepoznavanjem lica i mogućnošću praćenja uživo sa bilo kog mesta.
        """
    )
    st.write("**• HD/4K Rezolucija**")
    st.write("**• Noćno snimanje**")
    st.write("**• Pregled uživo**")

st.divider()
