import streamlit as st

st.set_page_config(
    page_title="ALFASAAT MEDIA DOO",
    page_icon="☀️",
    layout="wide"
)

# GLAVNA "HERO" SEKCIJA: Slika i tekst jedno pored drugog
# Pravimo dve kolone: leva za tekst, desna za sliku (odnos širine 3:2)
kolona_naslov, kolona_slika = st.columns([3, 2], vertical_alignment="center")

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
    # Ovde učitavamo sliku. Streamlit će je automatski prilagoditi veličini desne kolone
    try:
        st.image("solarni_paneli.jpg", use_container_width=True)
    except:
        st.info("Prikažite vašu novu sliku ovde.")

st.divider()

# ... OSTATAK VAŠEG KODA (Ko smo mi, Naše usluge, Kalkulator, Forma...)
