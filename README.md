# 🤖 Minecraft Plugin Helper

Asystent konfiguracyjny dla pluginów Minecraft — dostępny przez Streamlit (web) i Discord.

## 🔧 Funkcje

- Analiza i tłumaczenie plików konfiguracyjnych (np. `config.yml`)
- Sugestie poprawek, błędów YAML
- Integracja z Discordem: komenda `!plugin`

## 🚀 Uruchomienie lokalne

1. Stwórz plik `.env` z zawartością:

OPENAI_API_KEY="tgp_v1_7Jzy4PPSy3iZ4knffk8z9aVCav2vqIvC3yRJEY56dYs"
OPENAI_BASE_URL="https://api.together.xyz/v1"
DISCORD_BOT_TOKEN="aJFZgy-p34ULZs-kEE508qjTgUhYtkpd"

2. Zainstaluj zależności:

pip install -r requirements.txt

3. Uruchom aplikację web:

streamlit run streamlit_app.py

4. Uruchom bota Discord:
   
Skopiuj dane do `.streamlit/secrets.toml`:

OPENAI_API_KEY="tgp_v1_7Jzy4PPSy3iZ4knffk8z9aVCav2vqIvC3yRJEY56dYs"
OPENAI_BASE_URL="https://api.together.xyz/v1"
DISCORD_BOT_TOKEN="aJFZgy-p34ULZs-kEE508qjTgUhYtkpd"
