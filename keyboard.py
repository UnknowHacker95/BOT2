from telebot import types

button_1 = types.KeyboardButton('Подарок')
button_2 = types.KeyboardButton('Задание')
button_3 = types.KeyboardButton('Скука')
button_4 = types.KeyboardButton('Идеи')

mainkey = types.ReplyKeyboardMarkup()
mainkey.add(button_1).add(button_2).add(button_3).add(button_4)

button_ch_1 = types.KeyboardButton('1')
button_ch_2 = types.KeyboardButton('2')

chisla = types.ReplyKeyboardMarkup()
chisla.add(button_ch_1).add(button_ch_2)