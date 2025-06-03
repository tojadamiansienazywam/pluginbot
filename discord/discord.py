import os
import discord
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

llm = ChatOpenAI(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.3
)

@client.event
async def on_ready():
    print(f"Bot zalogowany jako {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!plugin"):
        query = message.content.removeprefix("!plugin").strip()
        await message.channel.typing()
        response = llm.invoke(query)
        await message.reply(response.content)

client.run(os.getenv("DISCORD_TOKEN"))
