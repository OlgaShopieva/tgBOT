import telebot
import random
from config import TOKEN
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton('Знак зодиака')
    item2 = telebot.types.KeyboardButton('Угадайка цифру')
    item3 = telebot.types.KeyboardButton('Стикеры')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выбери нужный вариант', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(mess):
    if mess.text == 'Знак зодиака':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1 = telebot.types.InlineKeyboardButton('Овен', callback_data='Овен')
        item2 = telebot.types.InlineKeyboardButton('Телец', callback_data='Телец')
        item3 = telebot.types.InlineKeyboardButton('Близнецы', callback_data='Близнецы')
        item4 = telebot.types.InlineKeyboardButton('Рак', callback_data='Рак')
        item5 = telebot.types.InlineKeyboardButton('Лев', callback_data='Лев')
        item6 = telebot.types.InlineKeyboardButton('Дева', callback_data='Дева')
        item7 = telebot.types.InlineKeyboardButton('Весы', callback_data='Весы')
        item8 = telebot.types.InlineKeyboardButton('Скорпион', callback_data='Скорпион')
        item9 = telebot.types.InlineKeyboardButton('Стрелец', callback_data='Стрелец')
        item10 = telebot.types.InlineKeyboardButton('Козерог', callback_data='Козерог')
        item11 = telebot.types.InlineKeyboardButton('Водолей', callback_data='Водолей')
        item12 = telebot.types.InlineKeyboardButton('Рыбы', callback_data='Рыбы')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(mess.chat.id, 'Нажимай на свой знак', reply_markup=markup)
    if mess.text == 'Угадайка цифру':
        input1 = bot.send_message(mess.chat.id, 'Загадано число от 1 до 3, попробуйте угадать')
        bot.register_next_step_handler(input1, num_generator)
    if mess.text == 'Стикеры':
        input2 = bot.send_message(mess.chat.id, 'Пришли цифру от 1 до 5 и я пришлю тебе стикер')
        bot.register_next_step_handler(input2, sticker_generator)



@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    dict_zodiac = sign_descrip()
    if call.data == 'Овен':
        bot.send_message(call.message.chat.id, dict_zodiac['Овен'])
    elif call.data == 'Телец':
        bot.send_message(call.message.chat.id, dict_zodiac['Телец'])
    elif call.data == 'Близнецы':
        bot.send_message(call.message.chat.id, dict_zodiac['Близнецы'])
    elif call.data == 'Рак':
        bot.send_message(call.message.chat.id, dict_zodiac['Рак'])
    elif call.data == 'Лев':
        bot.send_message(call.message.chat.id, dict_zodiac['Лев'])
    elif call.data == 'Дева':
        bot.send_message(call.message.chat.id, dict_zodiac['Дева'])
    elif call.data == 'Весы':
        bot.send_message(call.message.chat.id, dict_zodiac['Весы'])
    elif call.data == 'Скорпион':
        bot.send_message(call.message.chat.id, dict_zodiac['Скорпион'])
    elif call.data == 'Стрелец':
        bot.send_message(call.message.chat.id, dict_zodiac['Стрелец'])
    elif call.data == 'Козерог':
        bot.send_message(call.message.chat.id, dict_zodiac['Козерог'])
    elif call.data == 'Водолей':
        bot.send_message(call.message.chat.id, dict_zodiac['Водолей'])
    elif call.data == 'Рыбы':
        bot.send_message(call.message.chat.id, dict_zodiac['Рыбы'])

def sign_descrip():
    dict = {}
    with open('file.txt', 'r', encoding='utf-8') as f:
        for _ in range(12):
            str1 = f.readline().split(' ', 1)
            dict[str1[0]] = str1[1]
    return dict

def num_generator(messag):
    x = random.randint(0, 5)
    if messag.text == str(x):
        bot.send_message(messag.chat.id, f'Угадал! Число было {x}')
    else:
        bot.send_message(messag.chat.id, f'Не угадал! Число было {x}')

def sticker_generator(msg):
    if msg.text == '1':
        bot.send_sticker(msg.chat.id, 'CAACAgIAAxkBAAEHJphjuIHh9R2IJwIhn6usHtlhuiZ1agACYAUAAj-VzApGyHYEZMxRFS0E')
    if msg.text == '2':
        bot.send_sticker(msg.chat.id, 'CAACAgIAAxkBAAEHJppjuIHlvyrt9bdm_ebJSzrzCz1pBQACbgUAAj-VzAqGOtldiLy3NS0E')
    if msg.text == '3':
        bot.send_sticker(msg.chat.id, 'CAACAgIAAxkBAAEHJpxjuIHmVWeid-xjwc3fCTj9Dk0wPwACWgUAAj-VzAobFrmFvSDDnS0E')
    if msg.text == '4':
        bot.send_sticker(msg.chat.id, 'CAACAgIAAxkBAAEHJqBjuIHox3WHVFCutD2wciRCn1z58wACcAUAAj-VzArvDuYB7z8ley0E')
    if msg == '5':
        bot.send_sticker(msg.chat.id, 'CAACAgIAAxkBAAEHJqhjuIH5dGMLQyRGHsj7iSzVzgICewACcwUAAj-VzAo3ePzsWWk9My0E')




bot.polling(none_stop=True)
