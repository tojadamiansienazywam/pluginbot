import streamlit as st
from logic import analyze_input

st.set_page_config(page_title="Minecraft Plugin Helper")
st.title("🧩 Asystent pluginów Minecraft")

user_input = st.text_area("Wklej treść pliku lub zadaj pytanie:")

if st.button("🔍 Przeanalizuj") and user_input.strip():
    with st.spinner("Analizuję dane..."):
        result = analyze_input(user_input)
    st.markdown("---")
    st.markdown(f"**🧠 Odpowiedź:**\n\n{result}")