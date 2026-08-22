import streamlit as st

# 1. Podešavanje stranice
st.set_page_config(
    page_title="ALFASAAT MEDIA DOO",
    page_icon="☀️",
    layout="wide"
)

# 2. GLAVNA SEKCIJA: Tekst i slika sa logoom
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

# 3. SEKCIJA: Naše usluge prilagođene mobilnim telefonima (st.expander)
st.header("⚡ Naše ključne oblasti poslovanja")
st.write("Dodirnite oblast ispod da biste videli detalje i prednosti:")

# Prva usluga
with st.expander("☀️ SOLARNI PANELI", expanded=False):
    st.write("")
    st.write(
        """
        Kompletna rešenja za energetsku nezavisnost. Projektovanje, 
        montaža i održavanje solarnih elektrana za kuće i firme.
        
        * **• Smanjenje računa za struju do 90%**
        * **• Prelazak na čistu, zelenu energiju**
        * **• Ugradnja opreme vrhunskog kvaliteta sa garancijom**
        """
    )

# Druga usluga
with st.expander("🚨 ALARMNI SISTEMI", expanded=False):
    st.write("")
    st.write(
        """
        Najmoderniji protivprovalni sistemi i pametni alarmni uređaji 
        koji trenutno javljaju svaku opasnost direktno na vaš telefon.
        
        * **• Trenutna dojava na mobilnu aplikaciju**
        * **• Bežični i žični senzori pokreta i loma stakla**
        * **• Pouzdana zaštita objekta 24/7**
        """
    )

# Treća usluga
with st.expander("📹 VIDEO NADZOR", expanded=False):
    st.write("")
    st.write(
        """
        Profesionalne kamere visoke rezolucije sa pametnom analitikom, 
        prepoznavanjem lica i mogućnošću praćenja uživo sa bilo kog mesta.
        
        * **• Kristalno jasna HD i 4K rezolucija slika**
        * **• Napredno infracrveno i kolor noćno snimanje**
        * **• Pregled kamera uživo preko telefona ili računara**
        """
    )

st.divider()

# 4. SEKCIJA: Kontakt forma na dnu sajta
st.header("📩 Kontaktirajte nas")
st.write("Imate pitanje ili želite ponudu? Pišite nam direktno putem forme ispod.")

with st.form("kontakt_forma", clear_on_submit=True):
    ime = st.text_input("Vaše ime i prezime *")
    email = st.text_input("Vaša E-mail adresa *")
    telefon = st.text_input("Vaš broj telefona")
    
    usluga = st.selectbox(
        "Koja usluga vas najviše zanima?",
        ["Solarni paneli", "Alarmi", "Video nadzor", "Kompletno rešenje (Sve navedeno)"]
    )
    
    poruka = st.text_area("Vaša poruka ili specifični zahtevi *")
    
    posalji = st.form_submit_button("Pošalji upit")
    
    if posalji:
        if ime and email and poruka:
            st.success(f"Hvala Vam, {ime}! Vaš upit za uslugu '{usluga}' je uspešno primljen. Odgovorićemo vam u najkraćem roku.")
        else:
            st.error("Molimo vas da popunite obavezna polja (Ime, Email i Poruka).")
