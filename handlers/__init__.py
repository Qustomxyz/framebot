from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start(update, context):
    debug = False
    chat_id = str(update.message['chat']['id'])
    person = str(update.message['from_user']['id'])
    name = update.message['from_user']['first_name']

    print(dir(update.message))
    print(update.message['from_user'])

    my_message = f"Привет, {name}!\n\n" if name else "Привет!\n\n"
    my_button = InlineKeyboardButton(f"Здесь пока ничего нет"),
    update.message.reply_html(text=my_message, reply_markup=InlineKeyboardMarkup([my_button]))


def button(update, context):
    query = update.callback_query
    print(query)
