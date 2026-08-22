# 3. Sekcija: Tri glavna box-a (Usluge)
st.write("") # Prazan prostor za bolji vizuelni razmak
st.header("⚡ Naše ključne oblasti poslovanja")

# Kreiramo 3 kolone za tri box-a
box1, box2, box3 = st.columns(3)

# Prvi box: SOLARNI PANELI
with box1:
    with st.container(border=True):
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
    with st.container(border=True):
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
    with st.container(border=True):
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
