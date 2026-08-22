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

# 3. SEKCIJA: Tri ključne oblasti poslovanja
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
    st.info("✓ SMANJENJE RAČUNA\n\n✓ Najkvalitetniji paneli\n\n✓ Brza otplata investicije")
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
    st.subheader("🛡️ VIDEO (CCTV) NADZOR")
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

# 4. SEKCIJA: Pametni Kalkulator Uštede i Investicije (Korigovan font i matematika)
st.header("🧮 Orijentacioni proračun za solarne panele")
st.write("Unesite vaš prosečan mesečni račun za struju da biste videli optimalnu snagu, cenu investicije i uštedu.")

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
    
    # Realna inženjerska matematika za Srbiju
    prosecna_cena_kwh = 13.0
    potrosnja_kwh_mesecno = racun / prosecna_cena_kwh
    optimalna_mesecna_proizvodnja = potrosnja_kwh_mesecno * 0.75
    potrebna_snaga_prosek = optimalna_mesecna_proizvodnja / 100
    
    min_snaga = potrebna_snaga_prosek * 0.9
    max_snaga = potrebna_snaga_prosek * 1.1
    
    # Proračun investicije (Uprošćeno: ~1000 EUR po kW sistema sa montažom i papirima u RSD)
    cena_po_kw_rsd = 117000
    prosecna_snaga_za_investiciju = (min_snaga + max_snaga) / 2
    okvirna_investicija = int(prosecna_snaga_za_investiciju * cena_po_kw_rsd)
    
    # Realna godišnja ušteda (Smanjeno na 70% ukupnog godišnjeg računa zbog fiksnih stavki EPS-a)
    godisnja_usteda = int((racun * 12) * 0.70)

with kolona_kalk_rez:
    # Umesto st.metric koji pravi ogromne fontove, koristimo čist podrazumevani tekst (Boldovano)
    st.write(f"📋 **Preporučena snaga elektrane:** {min_snaga:.1f} - {max_snaga:.1f} kW")
    st.write(f"💰 **Orijentaciona cena investicije (ključ u ruke):** oko **{okvirna_investicija:,} RSD**")
    st.write(f"📉 **Procenjena godišnja ušteda na računu:** oko **{godisnja_usteda:,} RSD**")
    
    # Kratka računica otplate za klijenta
    period_otplate = okvirna_investicija / godisnja_usteda
    st.write(f"⏳ **Period otplate investicije:** cca **{period_otplate:.1f} godina** (nakon toga elektrana donosi čist profit)")
    
    st.caption("Napomena: Proračun je informativnog karaktera. Tačna cena zavisi od tehničkih uslova na krovu i odabira opreme.")

st.divider()

# 5. SEKCIJA: Kontakt forma
st.header("📩 Kontaktirajte nas")
st.write("Imate pitanje ili želite ponudu? Pišite nam direktno putem forme ispod.")

k_levo, k_sredina, k_desno = st.columns(3)

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
