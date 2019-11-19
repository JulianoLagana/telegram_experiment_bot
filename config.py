import os
import json
from telegram.ext import Updater
from telegram.ext import CommandHandler


def register_user(update, context, token):
    chat_id = update.effective_chat.id
    config = {'token': token, 'chat_id': chat_id}
    json.dump(config, open('telegram_config.json', 'w'))
    context.bot.send_message(chat_id=chat_id, text='You are now registered.')
    updater.is_idle = False


if not os.path.exists('telegram_config.json') or True:
    print("No configuration file could be found. Let's create a new one.")
    token = input("Please input the access token for the bot you would like to use for the updates:")

    updater = Updater(token=token, use_context=True)
    start_handler = CommandHandler('start', lambda u,c: register_user(u, c, token))
    updater.dispatcher.add_handler(start_handler)
    updater.start_polling()

    print('Now send the command /start to your bot so we can finish the configuration.')
    updater.idle()

    print('Great! Eveything is set up for you. Please wait while the bot is being stopped.')
    updater.stop()
