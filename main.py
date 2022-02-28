# Телеграмм бот версии 2.0 - имеет меню

import telebot  # pyTelegramBotAPI	4.3.1
from telebot import types

bot = telebot.TeleBot('5150353309:AAHW1DPdYWBmnLyYFHFmmFJpZPstV1wuwGo')  # Создаем экземпляр бота @Salakhov_Shamil_1MD25_bot
# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Главное меню')
    btn2 = types.KeyboardButton('Помощь')
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Йоу здорова, {0.first_name}! Я тестовый бот для курса программирования на языке Питон! "
                          "Пока еще я ничего не умею, но скоро буду.".format(message.from_user), reply_markup=markup)


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == 'Главное меню' or ms_text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Развлечения')
        btn2 = types.KeyboardButton('Камера')
        btn3 = types.KeyboardButton('Управление')
        back = types.KeyboardButton('Помощь')
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(chat_id, text='Вы в главном меню', reply_markup=markup)
    elif ms_text == 'Развлечения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Прислать собаку')
        btn2 = types.KeyboardButton('Прислать анекдот')
        back = types.KeyboardButton('Вернуться в главное меню')
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text='Развлечения', reply_markup=markup)
    elif ms_text == '/dog' or ms_text == 'Прислать собаку':
        img = open('putin.jpg', 'rb')
        bot.send_photo(message.chat.id, img)
        bot.send_message(chat_id, text='Это собака!')
    elif ms_text == 'Прислать анекдот':
        bot.send_message(chat_id, text='Какого размера кровать священника? Сложно? Да ладно вам, это ж любой ребенок знает')
    elif ms_text == 'Камера':
        bot.send_message(chat_id, text='Еще не готово...')
    elif ms_text == 'Управление':
        bot.send_message(chat_id, text='Еще не готово...')
    elif ms_text == 'Помощь' or ms_text == '/help':
        bot.send_message(chat_id, 'Автор: Салахов Шамиль')
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Напишите автору', url='https://t.me/debilsalakhov')
        btn2 = types.InlineKeyboardButton(text='Электронная почта автора', url='bigmoyka@gmail.com')
        btn3 = types.InlineKeyboardButton(text='Инста автора', url='https://www.instagram.com/debilsalakhov')
        key1.add(btn1, btn2, btn3)
        img = open('chad.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)
    else:
        bot.send_message(chat_id, text='Понял тебя. Ты написал: ' + ms_text)

# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()
