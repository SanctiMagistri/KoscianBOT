import discord

import scripts
def handle_response(message) -> str:
    p_message = message.lower()
    print(p_message)


    if p_message[:1] == "r":
        throw = scripts.check_command(p_message[2:])
        return str(throw)



    return "Co xD"
