import telebot
import pyowm

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc')
bot = telebot.TeleBot("953646504:AAGGcusriWInq-JQlNIbRdfVZE6wxBAq8PE")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#	bot.reply_to(message, "Howdy Ho, how are you doing?")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]

    answer = " In the city " + message.text + " now " + w.get_detailed_status() + "\n"
    answer += "Temperature now " + str(temp) + "\n\n"
    if temp < 10:
        answer += "The coldest"
    elif temp < 20:
        answer += "Very cold"
    else:
        answer += "Normally"

    bot.send_message(message.chat.id, answer)

try:
    bot.polling(none_stop=True, interval=0)
except Exception:
    pass
