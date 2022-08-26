from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hey", "hello", "yo"):
        return "Hey, how's it going?"

    if user_message in "who are you?":
        return "I'm Josh, a Bot!"

    if user_message in "time?":
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y,  %H:%M%S")
        return date_time

    return "Sorry... I don't understand"
