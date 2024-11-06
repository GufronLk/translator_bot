from data.loader import bot
from database.db import make_fav


@bot.callback_query_handler(func=lambda call: call.data.startswith('fav'))
def add(callback):
    _, translation_id = callback.data.split('_')

    make_fav(translation_id=int(translation_id))
    bot.answer_callback_query(callback.id, 'Добавлено в избранное')
