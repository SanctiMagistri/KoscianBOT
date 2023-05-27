import os

import discord
from discord.ext import commands
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


    async def send_message(message, user_message, is_private, is_hidden):
        try:
            if user_message == "hello there":
                picture = discord.File("general_kenobi.jpg")
                await message.channel.send(file=picture)
            elif user_message == "help":
                embed = discord.Embed(title="Kościan v0.4", color=discord.Color.dark_red(),description="Bot do rzucania kośćmi podczas sesji RPG!")
                embed.set_author(name="Sancti Magistri")
                embed.add_field(
                    name="Prefixy opcjonalne:",
                    value="`?` - Bot wysyła odpowiedź w wiadomości prywatnej.\n"
                          "`!` - Bot umieszcza wynik rzutu w spojlerze.")
                embed.add_field(name="Komendy:",
                                value="`komenda|aliasy` `<argument[opcjonalny argument]>` - Opis komend\n\n"
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
                    if is_private:
                        await message.author.send(response)
                    else:
                        if is_hidden:
                            await message.channel.send(f"<@{message.author.id}> ||" + response + "||")
                        else:
                            await message.channel.send(f"<@{message.author.id}> " + response)
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
            await send_message(message, user_message, is_private=True, is_hidden=False)
        else:
            if user_message[0] == '!':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=False, is_hidden=True)
            else:
                await send_message(message, user_message, is_private=False, is_hidden=False)

    client.run(TOKEN)

run_bot()