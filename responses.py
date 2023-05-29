import scripts
def handle_response(message) -> str:
    p_message = message.lower()

    if p_message[:2] == "r ":
        throw = scripts.standard_throw(p_message[2:])
        return str(throw)
    if p_message[:5] == "roll ":
        throw = scripts.standard_throw(p_message[5:])
        return str(throw)

    if p_message[:2] == "t ":
        throw = scripts.TFTL_throw(p_message[2:])
        return str(throw)
    if p_message[:5] == "tftl ":
        throw = scripts.TFTL_throw(p_message[5:])
        return str(throw)
    if p_message[:6] == "tales ":
        throw = scripts.TFTL_throw(p_message[6:])
        return str(throw)

    return ""
