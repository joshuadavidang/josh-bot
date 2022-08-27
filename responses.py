from datetime import datetime


def bot_to_human(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hey", "hi", "hey!", "hello", "yo"):
        return "Hey, how's it going?"

    if user_message in "who are you?":
        return "I'm Josh, a Bot!"

    if user_message in "time?":
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y,  %H:%M%S")
        return date_time

    if user_message in "schedule":
        now = datetime.now()
        day = now.strftime("%w")

        result = ""

        if day == "0":
            result = "Its Sunday... get some rest!"

        elif day == "1":
            result = "You have a class today at 12pm - IS110. Have you pre-read the content?"

        elif day == "2":
            result = "You have a class today at 8am - COR-STAT-1202"

        elif day == "3":
            result = "You have a class today at 3.30pm - LTB"

        elif day == "4":
            result = "You have a class today at 8am - IS111"

        elif day == "5":
            result = "TGIF! You have no class today."

        elif day == "6":
            result = "Its Saturday... get some rest!"

        return result

    return "Sorry, I don't understand."
