import constants as keys
from telegram.ext import *
import responses as r

print("Bot has started...")


def start_command(update, context):
    update.message.reply_text("Type something random to get started!")


def help_command(update, context):
    update.message.reply_text("Google if you need help!")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)


def handle_error(update, context):
    print(f"Update caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(handle_error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()