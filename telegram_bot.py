from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
import telebot

bot = telebot.TeleBot("1327360961:AAGea4wpJuifaqERTKUtmvwwTpEyilYAizw")
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('71bff50aeaf49f58b00382d0c8294c8e', config_dict)
mgr = owm.weather_manager()




@bot.message_handler(content_types=['text'])
def send_echo(message):
 try:
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = int(w.temperature('celsius')["temp"])
    status = (w.detailed_status)
    answer = "В городе " + message.text + " сейчас " + str(status) + "\n"
    answer += "Температура сейчас в районе " + str(temp) + " градусов " + "\n\n"
    if temp<=10:
        answer += ("На улице холодно, одевай куртку")
    elif temp<=0:
        answer += ("На улице очень холодно, одень тёплую куртку")
    elif (temp>10) and( temp<20):
        answer += ("На улице прохладно, одень ветровку")
    elif temp>=20:
        answer += ("На улице жарко, надень футболку и шорты")

    bot.send_message(message.chat.id, answer)

 except:
    bot.send_message(message.chat.id,'Ошибка! Город не найден.')
bot.polling( none_stop = True)
input()