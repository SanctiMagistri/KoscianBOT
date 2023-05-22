import scripts
def handle_response(message) -> str:
    p_message = message.lower()
    print(p_message)

    if p_message == "hello there":
        return "General Kenobi!"

    if p_message[:4] == "roll" or p_message[:4] == "rzut":
        throw = scripts.check_command(p_message[5:])
        return str(throw)



    return "Co xD"
