import streamlit as st

# 1. Podešavanje stranice
st.set_page_config(
    page_title="ALFASAAT MEDIA DOO",
    page_icon="☀️",
    layout="wide"
)

# 2. GLAVNA SEKCIJA: Vaš tekst i slika sa logoom
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

# 3. SEKCIJA: Tri ključne oblasti poslovanja (Pobednička verzija sa slike)
st.header("⚡ Naše ključne oblasti poslovanja")
st.write("") 

b1, b2, b3 = st.columns(3)

with b1:
    st.markdown("### ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    st.subheader("☀️ SOLARNI PANELI")
    st.caption("Energetska nezavisnost za dom i privredu")
    st.write(
        """
        Kompletna rešenja po sistemu ključ u ruke. Projektovanje, 
        vrhunska montaža i dugogodišnje održavanje solarnih elektrana.
        """
    )
    st.info("✓ Smanjenje računa do 90%\n\n✓ Najkvalitetniji paneli\n\n✓ Brza otplata investicije")
    st.markdown("### ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

with b2:
    st.markdown("### ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    st.subheader("🚨 ALARMNI SISTEMI")
    st.caption("Pametna zaštita imovine 24/7")
    st.write(
        """
        Najmoderniji protivprovalni sistemi i pametni alarmni uređaji 
        koji trenutno javljaju svaku opasnost i pokušaj upada.
        """
    )
    st.info("✓ Trenutna dojava na telefon\n\n✓ Bežični senzori pokreta\n\n✓ Potpuna kontrola pristupa")
    st.markdown("### ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

with b3:
    st.markdown("### ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
    st.subheader("📹 VIDEO NADZOR")
    st.caption("Profesionalna kontrola sa bilo kog mesta")
    st.write(
        """
        Kamere visoke rezolucije sa pametnom analitikom, 
        prepoznavanjem lica i mogućnošću praćenja u realnom vremenu.
        """
    )
    st.info("✓ Kristalno jasna 4K slika\n\n✓ Napredno noćno snimanje\n\n✓ Pregled uživo preko aplikacije")
    st.markdown("### ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

st.divider()

# 4. SEKCIJA: Pametni Kalkulator Uštede
st.header("🧮 Izračunajte uštedu za solarne panele")
st.write("Unesite vaš prosečan mesečni račun za struju i saznajte okvirnu snagu sistema koja vam je potrebna.")

kolona_kalk_unos, kolona_kalk_rez = st.columns(2, vertical_alignment="center")

with kolona_kalk_unos:
    racun = st.number_input(
        "Prosečan mesečni račun za struju (u dinarima):", 
        min_value=3000, 
        max_value=150000, 
        value=9000, 
        step=500,
        key="kalk_racun"
    )
    cena_kwh = 14  
    potrosnja_kwh = racun / cena_kwh
    potrebna_snaga = potrosnja_kwh / 105  
    godisnja_usteda = racun * 12

with kolona_kalk_rez:
    metrika1, metrika2 = st.columns(2)
    with metrika1:
        st.metric(label="Preporučena snaga elektrane", value=f"{potrebna_snaga:.1f} kW")
    with metrika2:
        st.metric(label="Orijentaciona godišnja ušteda", value=f"{godisnja_usteda:,} RSD")
    st.caption("Napomena: Proračun je informativnog karaktera.")

st.divider()

# 5. SEKCIJA: Kontakt forma (Sa suženim poljima na PC-u pomoću tri kolone)
st.header("📩 Kontaktirajte nas")
st.write("Imate pitanje ili želite ponudu? Pišite nam direktno putem forme ispod.")

# Trik: Pravimo odnos kolona 1:2:1. Sadržaj ide u srednju kolonu koja je 50% širine ekrana.
# Na mobilnim uređajima, Streamlit će ovu srednju kolonu raširiti na 100%, pa forma ostaje idealna i na telefonu!
k_levo, k_sredina, k_desno = st.columns([1, 2, 1])

with k_sredina:
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
                st.success(f"Hvala Vam, {ime}! Vaš upit je uspešno primljen. Odgovorićemo vam u najkraćem roku.")
            else:
                st.error("Molimo vas da popunite obavezna polja (Ime, Email i Poruka).")

st.divider()

# 6. SEKCIJA: Podnožje sajta (Footer) sa pravnim podacima
f1, f2, f3 = st.columns(3)

with f1:
    st.subheader("ALFASAAT MEDIA DOO")
    st.caption("Pouzdan partner za bezbednost i zelenu energiju.")

with f2:
    st.write("**📍 Kontakt podaci:**")
    st.write("📱 Telefon: +381 XX XXX XXX")
    st.write("📧 E-mail: info@alfasaat.com")
    st.write("🕒 Radno vreme: Pon - Pet: 08:00 - 16:00")

with f3:
    st.write("**📄 Pravne informacije:**")
    st.write("Matični broj: XXXXXXXX")
    st.write("PIB: XXXXXXXXX")
    st.write("Sedište: Srbija")
