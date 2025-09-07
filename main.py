import streamlit as st

st.set_page_config(page_title="VIS Rechner", page_icon="🧮")
st.title("VIS Rechner")
st.subheader("Vasoactive Inotropic Score")

with st.form("vis_form"):
    # Basisdaten
    gewicht = st.number_input("Gewicht (kg)", min_value=0.0, value=70.0, step=0.5, format="%.1f")

    # Dosierungen in den gewünschten klinischen Einheiten
    ne = st.number_input("Norepinephrin (µg/kg/min)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
    vaso_u_h = st.number_input("Vasopressin (U/h)", min_value=0.0, value=0.0, step=0.1, format="%.2f")
    methylenblau = st.number_input("Methylenblau (mg/kg/h)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
    epi = st.number_input("Epinephrin (µg/kg/min)", min_value=0.0, value=0.0, step=0.01, format="%.2f")
    milrinon = st.number_input("Milrinon (µg/kg/min)", min_value=0.0, value=0.0, step=0.1, format="%.2f")
    dobutamin = st.number_input("Dobutamin (µg/kg/min)", min_value=0.0, value=0.0, step=0.1, format="%.1f")
    levosimendan = st.number_input("Levosimendan (µg/kg/min)", min_value=0.0, value=0.0, step=0.001, format="%.2f")

    berechnen = st.form_submit_button("Berechnen")

if 'vis' not in st.session_state:
    st.session_state['vis'] = 0.0

if berechnen:
    # Umrechnung Vasopressin: U/h -> U/kg/min
    if gewicht and gewicht > 0:
        vaso_u_kg_min = (vaso_u_h / gewicht) / 60.0
    else:
        vaso_u_kg_min = 0.0

    vis = (
        100.0 * ne +
        10_000.0 * vaso_u_kg_min +
        20.0 * methylenblau +
        100.0 * epi +
        10 * milrinon +
        1.0 * dobutamin +
        50.0 * levosimendan
    )
    st.session_state['vis'] = vis

st.metric("VIS-Score", f"{st.session_state['vis']:.0f}")

st.info(
    """Ein VIS von über ca. 30 wird häufig als kritischer Schwellenwert angesehen, oberhalb dessen die Mortalität erheblich steigt. 
    \n Ab einem VIS-Score von über 34 sollte über eine V-A-ECMO nachgedacht werden"""
)