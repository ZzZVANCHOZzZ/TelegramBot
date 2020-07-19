import pyowm
import telebot

bot = telebot.TeleBot("1327360961:AAGea4wpJuifaqERTKUtmvwwTpEyilYAizw")
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('71bff50aeaf49f58b00382d0c8294c8e')




@bot.message_handler(content_types=['text'])
def send_echo(message):
 try:
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = int(w.get_temperature('celsius')["temp"])
    status = w.get_detailed_status()
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