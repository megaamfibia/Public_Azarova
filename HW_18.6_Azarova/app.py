import telebot
from config import keys, TOKEN
from extensions import ConvertionException, MyConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def cmd_help(message: telebot.types.Message):
    text = "Чтобы начать работу, введите команду в следующем формате: \n <название валюты> <в какую валюту перевести> \
<количество переводимой валюты> \n Чтобы посмотреть список доступных валют, введите команду /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["audio", "document", "photo", "sticker", "video", "video_note", "voice", "location",
                                    "contact"])
def all_messages(message: telebot.types.Message):
    text = "Чтобы начать работу, введите запрос в следующем формате: \n <название валюты> <в какую валюту перевести> \
<количество переводимой валюты> \n Чтобы посмотреть список доступных валют, введите команду /values"
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    insert_values = message.text.split(' ')

    try:
        if len(insert_values) < 3:
            raise ConvertionException('недостаточно данных')
        if len(insert_values) > 3:
            raise ConvertionException('некорректные вводные данные. \n\nВведите запрос в следующем формате: \n '
                                      '<название валюты> <в какую валюту перевести> <количество переводимой валюты>')
        quote, base, amount = insert_values
        get_price = MyConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка: {e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка: не удалось обработать запрос. \n"{e}"\n\nВведите запрос в следующем формате: '
                              f'\n<название валюты> <в какую валюту перевести> <количество переводимой валюты>')
    else:
        text = f'Стоимость {amount} {quote} - {get_price} {base}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
