# Вариант 1 - самый простой чат бот, просто отзывается

import telebot  # pyTelegramBotAPI	4.3.1

bot = telebot.TeleBot('5150353309:AAHW1DPdYWBmnLyYFHFmmFJpZPstV1wuwGo')  # Создаем экземпляр бота @Salakhov_Shamil_1MD25_bot
# -----------------------------------------------------------------------
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     text="Йоу здорова, {0.first_name}! Я тестовый бот для курса программирования на языке Питон! "
                          "Пока еще я ничего не умею, но скоро буду.".format(message.from_user))


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    bot.send_message(chat_id, text="Понял тебя. Ты написал: " + ms_text)


# -----------------------------------------------------------------------
bot.polling(none_stop=True, interval=0)  # Запускаем бота

print()
