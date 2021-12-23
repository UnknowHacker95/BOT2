import telebot
import keyboard as kb
API_TOKEN = ''  # TODO: Вставьте сюда API_TOKEN вашего бота
day = []
answer =[]
bot = telebot.TeleBot(API_TOKEN)
controller = {}
INVALID_CHOICE = "Введите, пожалуйста, другой вариант - одно число из списка вариантов выше."
START_STICKER = 'CAACAgIAAxkBAAEDXxlhofzUZFEJyfjn7t2vosr1YR60tgACiwIAAladvQr3tGImDY878yIE'
WIN_STICKER = 'CAACAgIAAxkBAAEDAAE9YVgzvRi4Ej8ZNzxQnx2xqK0-Y6QAAooCAAJWnb0KPlJuixPFQGchBA'
BAD_STICKER = 'CAACAgIAAxkBAAEDAAE1YVgzgtRTh16cvcMIxKSSJjOWcU0AAiQLAAIEv_FLFuD22fNmUL0hBA'
WAIT_STICKER = 'CAACAgIAAxkBAAEDU4dhmMg7t8g7pvSYosWeZR571OBUBAACMgADmWuhLT0uAyXSw_MmIgQ'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id, START_STICKER)
    bot.send_message(message.from_user.id, """
    Привет! Это твой онлайн адвент-календарь!
    Совсем скоро Новый Год, а это значит, что приближается пора радости, веселья и отдыха!
    Обычно мы дарим подарки знакомым и близким, но иногда нужно радовать себя?;)
    Этот календарь рассчитан на 5 дней! 5 дней праздника!
    Заходи ко мне каждый день и открывай подарки!
    P.S. Я также даю загадки и ссылки на ресурсы, когда тебе скучно. Могу подбросить еще и идей для новогодних подарков!
    """, reply_markup=kb.mainkey)
    id = message.from_user.id
    day[id] = 'start'


@bot.message_handler(content_types=['text'])
def start(message):
    id = message.from_user.id
    choice = message.text
    day = controller.get(id, 'start') # Если вдруг такой user_id не сохранен, то считаем, что статус = start
    #answer = 'none'
    if day == 'start':
        answer = ch(id, choice)
    if day == '1':
        answer = ch(id, choice)
    if day == '2':
        answer = ch(id, choice)
    if day == '3':
        answer = ch(id, choice)
    if day == '4':
        answer = ch(id, choice)
    if day == '5':
        answer = ch(id, choice)
    bot.send_message(message.from_user.id, answer[0], reply_markup=answer[1])

def ch(user_id, user_choice):
    if user_choice != day[user_id]:
        return ["Не жульничай! Возвращайся завтра!", kb.chisla]
    if user_choice == 'start':
        day[user_id] = '1'
        return ["Твой первый день начинается завтра!)", kb.chisla]
    if user_choice == '1':
        day[user_id] == '2'
        return["""
    Праздник к нам приходит,
    Праздник к нам приходит,
    Праздник к нам приходит
    Всегда с Coca-Cola!
    Веселье приносит
    И вкус бодрящий
    Праздник на вкус
    Всегда настоящий!""", kb.chisla]
    if user_choice == '2' or user_choice == '3' or user_choice == '4' or user_choice == '5':
        pass
    return [INVALID_CHOICE, None]




bot.polling()