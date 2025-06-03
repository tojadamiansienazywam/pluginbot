from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os

# Inicjalizacja modelu AI
llm = ChatOpenAI(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.2,
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Jesteś ekspertem od pluginów Minecraft. Pomagasz użytkownikom konfigurować pliki YAML oraz rozwiązywać problemy z pluginami."),
    ("user", "{input}")
])

chain = prompt | llm

def analyze_input(user_text: str):
    try:
        response = chain.invoke({"input": user_text})
        return response.content
    except Exception as e:
        return f"❌ Błąd przetwarzania: {str(e)}"