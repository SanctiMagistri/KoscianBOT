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
            elif user_message == "help":
                embed = discord.Embed(title="Kościan v0.3", color=discord.Color.dark_red(),description="Bot do rzucania kośćmi podczas sesji RPG!")
                embed.set_author(name="Sancti Magistri")
                embed.add_field(
                    name="Prefixy opcjonalne:",
                    value="`?` - Bot wysyła odpowiedź w wiadomości prywatnej.")
                embed.add_field(name="Komendy:",
                                value="`komenda|aliasy` `<argument[opcjonalny argument]>` - Opis komend\n"
                                      "`help` - Strona pomocy\n"
                                      "`hello there` - ( ͡° ͜ʖ ͡°)\n"
                                      "`r|roll` `<XkY[+Z]?` lub `<XdY[+Z]>` (X - liczba kości, Y - typ kości, Z - opcjonalny bonus lub dodatkowe rzuty) - Standardowy rzut kością\n"
                                      "`tftl|tales|t` `<X>` (X - liczba kości) - Rzut kością k6 dla systemu TFTL\n",
                                inline=False)
                embed.set_footer(text="Wszelkie problemy i zażalenia proszę zgłaszać do /dev/null")
                await message.channel.send(embed=embed)
            else:
                response = responses.handle_response(user_message)
                if response != '':
                    await message.author.send(response) if is_private else await message.channel.send(response)
                else:
                    pass
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