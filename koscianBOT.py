import os

import discord
from dotenv import load_dotenv

def run_bot():
    load_dotenv()
    TOKEN = os.environ['DISCORD_TOKEN']
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} Podłączono')

    client.run(TOKEN)

run_bot()