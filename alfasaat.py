import streamlit as st

# 1. Podešavanje stranice (Naslov u tabu browsera i široki prikaz)
st.set_page_config(
    page_title="ALFASAAT MEDIA DOO",
    page_icon="☀️",
    layout="wide"
)

# 2. Glavni Baner (Zamenjuje CSS pozadinu - čisto i responzivno)
# Postavite vašu sliku solarnih panela ovde
try:
    st.image("solarni_paneli.jpg", use_container_width=True)
except:
    # Ako slika još nije u folderu, prikazuje se plavi info boks da kod ne pukne
    st.info("Ovde će se prikazati vaša glavna slika solarnih panela (solarni_paneli.jpg).")

# 3. Naslov i podnaslov firme
st.title("ALFASAAT MEDIA DOO")
st.subheader("Vaš partner za energetsku efikasnost i maksimalnu bezbednost")

# Kratka linija razdvajanja
st.divider()

# 4. Sekcija: O nama (Korišćenje kontejnera za lepši raspored)
with st.container():
    st.header("Ko smo mi?")
    st.write(
        """
        ALFASAAT MEDIA DOO je specijalizovana firma posvećena uvođenju modernih 
        tehnoloških rešenja u vaš dom i poslovanje. Naš cilj je da vam omogućimo 
        energetsku nezavisnost uz najviši nivo sigurnosti.
        """
    )

st.divider()

# 5. Sekcija: Naše usluge (Pravljenje dve čiste kolone bez HTML-a)
st.header("Naše glavne usluge")

kolona_solari, kolona_bezbednost = st.columns(2)

with kolona_solari:
    st.subheader("☀️ Solarni Paneli")
    st.write(
        """
        - Projektovanje i ugradnja solarnih elektrana.
        - Ključ u ruke za domaćinstva i industrijske objekte.
        - Smanjenje računa za struju i prelazak na zelenu energiju.
        - Korišćenje opreme vrhunskog kvaliteta sa dugogodišnjom garancijom.
        """
    )
    # Čisto Python dugme koje menja boju na osnovu config.toml fajla
    st.button("Zatražite ponudu za panele", key="btn_solari")

with kolona_bezbednost:
    st.subheader("🛡️ Video nadzor i Alarmi")
    st.write(
        """
        - Montaža profesionalnih sistema video nadzora visoke rezolucije.
        - Instalacija pametnih alarmnih sistema sa dojavom na mobilni telefon.
        - Kontrola pristupa i integracija svih sistema u jednu aplikaciju.
        - Održavanje i tehnička podrška 24/7.
        """
    )
    st.button("Zatražite ponudu za bezbednost", key="btn_security")

st.divider()

# 6. Sekcija: Kontakt forma (Čist Python interaktivni element)
st.header("📩 Kontaktirajte nas")

with st.form("kontakt_forma", clear_on_submit=True):
    ime = st.text_input("Vaše ime i prezime")
    email = st.text_input("Vaša E-mail adresa")
    usluga = st.selectbox(
        "Komercijalna usluga koja vas zanima",
        ["Solarni paneli", "Video nadzor i alarmi", "Kompletno rešenje (Sve navedeno)"]
    )
    poruka = st.text_area("Vaša poruka ili specifični zahtevi")
    
    # Dugme za slanje unutar forme
    posalji = st.form_submit_button("Pošalji upit")
    
    if posalji:
        if ime and email and poruka:
            # Ovde kasnije možemo dodati kod za slanje maila, za sada samo potvrda
            st.success(f"Hvala Vam, {ime}! Vaš upit za uslugu '{usluga}' je uspešno evidentiran. Odgovorićemo vam u najkraćem roku.")
        else:
            st.error("Molimo vas da popunite sva obavezna polja (Ime, Email, Poruka).")
