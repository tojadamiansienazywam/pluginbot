import os
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Wczytaj zmienne środowiskowe
load_dotenv()

# Konfiguracja modelu LLM (Together.ai)
llm = ChatOpenAI(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.3,
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# Interfejs Streamlit
st.set_page_config(page_title="Minecraft Plugin Bot", page_icon="🛠️")
st.title("🛠️ Minecraft Plugin Bot")
st.markdown("Pomocnik AI do analizy i modyfikacji plików `config.yml` oraz ogólnej konfiguracji pluginów.")

# Tryb działania
mode = st.radio("Wybierz tryb pracy bota:", ["🔧 Modyfikacja pliku", "💬 Konwersacja o pluginach"])

if mode == "🔧 Modyfikacja pliku":
    uploaded_file = st.file_uploader("Wgraj plik `config.yml` pluginu", type=["yml", "yaml"])
    user_instruction = st.text_area("Co chcesz, aby bot zrobił z tym plikiem?",
                                     placeholder="Przykład: Dodaj nową rangę Mag z permisją essentials.kit.mag")

    if uploaded_file and user_instruction:
        yaml_content = uploaded_file.read().decode("utf-8")

        # Przygotuj prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Jesteś ekspertem od pluginów do Minecrafta. Twoim zadaniem jest analizować i modyfikować pliki config.yml. Odpowiadasz zawsze po polsku."),
            ("user", "Użytkownik chce wykonać następującą operację: {instruction}\n\nOto aktualna treść pliku konfiguracyjnego:\n\n{config}\n\nWygeneruj zmodyfikowaną wersję pliku YAML, bez tłumaczenia ani wyjaśnień, tylko sam plik YAML.")
        ])

        chain = prompt | llm
        response = chain.invoke({
            "instruction": user_instruction,
            "config": yaml_content
        })

        st.subheader("📄 Zmodyfikowany plik YAML")
        st.code(response.content, language="yaml")

        st.download_button(
            label="💾 Pobierz zmodyfikowany plik",
            data=response.content,
            file_name="config_modified.yml",
            mime="text/yaml"
        )

if mode == "💬 Konwersacja o pluginach":
    st.markdown("Zadaj dowolne pytanie dotyczące konfiguracji pluginów Minecraft.")
    user_question = st.text_area("Twoje pytanie:", placeholder="Np. Jak ustawić prefiks rangi w PowerRanks?")

    if user_question:
        qa_prompt = ChatPromptTemplate.from_messages([
            ("system", "Jesteś ekspertem od pluginów Minecraft. Odpowiadasz zawsze po polsku na pytania związane z konfiguracją popularnych pluginów."),
            ("user", "{question}")
        ])

        qa_chain = qa_prompt | llm
        answer = qa_chain.invoke({"question": user_question})

        st.subheader("🧠 Odpowiedź:")
        st.write(answer.content)