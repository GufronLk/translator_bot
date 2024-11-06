# pytelegrambotapi
# python-dotenv
# googletrans==4.0.0rc1
# pip install googletrans 3.0.0

# Перевод, История

from data.loader import bot


def main():
    from handlers import commands, texts, callbacks

    print('bot working')
    bot.infinity_polling()

# история ваших переводов
main()