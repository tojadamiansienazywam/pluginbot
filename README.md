# 🤖 Minecraft Plugin Helper

Asystent konfiguracyjny dla pluginów Minecraft — dostępny przez Streamlit (web) i Discord.

## 🔧 Funkcje

- Analiza i tłumaczenie plików konfiguracyjnych (np. `config.yml`)
- Sugestie poprawek, błędów YAML
- Integracja z Discordem: komenda `!plugin`

## 🚀 Uruchomienie lokalne

1. Stwórz plik `.env` z zawartością:

OPENAI_API_KEY="..."
OPENAI_BASE_URL="https://api.together.xyz/v1"
DISCORD_BOT_TOKEN="..."

2. Zainstaluj zależności:

pip install -r requirements.txt

3. Uruchom aplikację web:

streamlit run streamlit_app.py

4. Uruchom bota Discord:
   
Skopiuj dane do `.streamlit/secrets.toml`:

OPENAI_API_KEY="..."
OPENAI_BASE_URL="https://api.together.xyz/v1"
DISCORD_BOT_TOKEN="..."
