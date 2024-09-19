import telebot

bot = telebot.TeleBot('7239294300:AAHJFTJ_iwk7z4rs0AtMIQ79x_SouLcgV_I')


commands = [
    telebot.types.BotCommand('start', 'Почати спілкування з ботом'),
    telebot.types.BotCommand('menu', 'Показати меню'),
    telebot.types.BotCommand('help', 'Отримати допомогу'),
]

bot.set_my_commands(commands)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Вітаю {message.from_user.first_name}!\nВідкрити меню-/menu')

@bot.message_handler(commands=['menu'])
def menu(message):
    bot.send_message(message.chat.id, 'Отримати допомогу - /help')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Якщо у Вас залишились якісь запитання Ви можете неписати нашому адміністратору @000\n\nВідкрити меню-/menu')


@bot.message_handler(func=lambda message: True)
def info(message):
    if message.text.lower() in ['вітаю', 'доброго дня', 'доброг ранку', 'доброг вечора', 'доброї ночі']:
        bot.send_message(message.chat.id, f'Вітаю {message.from_user.first_name}!')
    else:
        bot.send_message(message.chat.id, 'Виберіть команду у меню -/menu')

bot.polling(non_stop=True)