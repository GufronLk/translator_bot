from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def fav_button(translation_id):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(text='Добавить в избранное',
                             callback_data=f'fav_{translation_id}')
    )
    return kb