import os

import discord
from dotenv import load_dotenv

import responses


def run_bot():
    load_dotenv()
    TOKEN = os.environ['DISCORD_TOKEN']
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} Podłączono')

    async def send_message(message, user_message, is_private):
        try:
            if user_message == "hello there":
                picture = discord.File("general_kenobi.jpg")
                await message.channel.send(file=picture)
            else:
                response = responses.handle_response(user_message)
                await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(e)
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)

run_bot()