import telebot
from telebot import types
import settings
from registruser import RegisterUser
from collections import deque,ChainMap
import parserweather as pw


list_users = deque()
bot = telebot.TeleBot(settings.API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    reg_user = RegisterUser()
    reg_user.set_user_info(message.from_user.first_name,message.from_user.id)
    list_users.append(ChainMap(reg_user.get_info_user()))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Добавить свой город')
    button2 = types.KeyboardButton('Узнать погоду в другом городе')
    markup.add(button1,button2)
    #bot.send_message(message.from_user.id,'Выберите какую кнопку нажать! ',reply_markup=markup)
    bot.send_message(message.from_user.id,f'{message.from_user.first_name.title()}  вы зарегистрированы.   Выберите какую кнопку нажать! ',reply_markup=markup)
    
    
        

@bot.message_handler(content_types=['text'])
def answer_on_message(message):
    print(list_users)
    if message.text.lower() == 'добавить свой город':
        for dict_user in list_users:
            if message.from_user.id in list(dict_user.values()) and None in list(dict_user.values()):
                print(list(dict_user.values()))
                break
        bot.send_message(message.from_user.id,'Введите свой город вначале добавь город')
    elif message.text.lower() == 'узнать погоду в другом городе' or message.text.lower() == 'погода в другом городе':
        bot.send_message(message.from_user.id,'Введите город и в конце добавь /')
    
    elif '/' in message.text:
        bot.send_message(message.from_user.id,pw.get_weather_city(pw.get_city_url(message.text)))

    elif  'город' in message.text.lower():
        for dict_user in list_users:
            if message.from_user.id in list(dict_user.values()):
                print(list(dict_user.values()))
                dict_user['city'] = message.text.split(' ')[1].title()
                print(dict_user)
                break
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('Погода в моем городе')
        button2 = types.KeyboardButton('Погода в другом городе')
        markup2.add(button1,button2)
        bot.send_message(message.from_user.id,f'Ваш город {message.text.title()}',reply_markup=markup2)
    
        

bot.polling()

