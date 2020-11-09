import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from handlers import start, button

load_dotenv()

# settings
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(os.environ.get("TOKEN"))


URL_ADDON = os.environ.get('URL_ADDON')
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=URL_ADDON)

HOOK_URL = os.environ.get("HOOK_URL")
updater.bot.set_webhook(HOOK_URL + URL_ADDON)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.idle()
