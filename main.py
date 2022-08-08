import random
import telebot
from telebot import types
import geopy.distance


a = 0

token = '2084950457:AAFHmbs-Sn6H3plEe0bh0A2YZ1kr7G04YVA'

bot = telebot.TeleBot(token=token)

dct = {}
dct_new = {}
lst_name = []

@bot.message_handler(commands=['start'])

def strat(message):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=3)
    button1 = types.KeyboardButton(text='Sport')
    button2 = types.KeyboardButton(text='Англ')
    button3 = types.KeyboardButton(text='Сповіщення')
    buttons.add(button1, button2, button3)

    button_from_user = bot.send_message(message.chat.id, text='З чого почнемо?🙃',
                                        reply_markup=buttons)
    bot.register_next_step_handler(button_from_user, perevirka)


def perevirka(message):
    if message.text == 'Англ':
        first(message)
    elif message.text == 'Sport':
        sport(message)
    elif message.text == 'Сповіщення':
        func_for_notification(message)

def first(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add('Так')
    bot.send_photo(message.chat.id, open('hi.jpg', 'rb'))
    send = bot.send_message(message.chat.id, 'Привіт🦖Я динозавр Dinorrr, який живе у IT світі👾' \
                                             '\nПропоную тобі пройти Дііінотест на знання англійської🏴' \
                                             '\n󠁧󠁢󠁥󠁮󠁧󠁿Ти зі мною?⬇️', reply_markup=keyboard)
    bot.register_next_step_handler(send, main_func)


def main_func(message):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=3)
    button1 = types.KeyboardButton(text='Test')
    button2 = types.KeyboardButton(text='Test2')
    button3 = types.KeyboardButton(text='Test3')
    buttons.add(button1, button2, button3)
    bot.send_photo(message.chat.id, open('CELECT.jpg', 'rb'))
    button_from_user = bot.send_message(message.chat.id, text='Вибирай тест ☺️',
                                        reply_markup=buttons)
    bot.register_next_step_handler(button_from_user, func_after_main)


def func_after_main(message):
    if message.text == 'Test':
        func_for_test(message)


def func_for_test(message):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=2)
    button3 = types.KeyboardButton(text='Start')
    buttons.add(button3)
    button_from_user = bot.send_message(message.chat.id, text='Цей тест розраховнаий на 10 хв\n Стартуємо!',
                                        reply_markup=buttons)
    bot.register_next_step_handler(button_from_user, func_start_test)


def func_start_test(message):
    if message.text == 'Start':
        bot.send_photo(message.chat.id, open('lets_s.jpg', 'rb'))
        func_test(message)


def func_test(message):
    global dct
    global keys
    global num
    global cor_ans
    cor_ans = 0
    dct = {}
    with open('answer.txt', 'r', encoding="utf-8") as file:
        q = 0
        for i in file.readlines():
            lst = i.strip().split('*')
            dct[lst[0]] = lst[1].strip('[]').split(",")
            q = q + 1
            if q == 30:
                break
    num = 1
    keys = list(dct.keys())
    func_for_random(message)


def func_for_random(message):
    global qes
    qes = random.choice(keys)
    if num == 20:
        bot.send_photo(message.chat.id, open('end.jpg', 'rb'))
        bot.send_message(message.chat.id, text='Ви пройшли тест!')
        print('Ви пройшли тест')
        func_the_end(message)
    else:
        func_start(message)


def func_start(message):
    global num
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    button1 = types.KeyboardButton(text=f'{dct[qes][0]}')
    button2 = types.KeyboardButton(text=f'{dct[qes][1]}')
    button3 = types.KeyboardButton(text=f'{dct[qes][2]}')
    buttons.add(button1, button2, button3)
    button_from_user = bot.send_message(message.chat.id, f'{num}){qes}', reply_markup=buttons)
    num = num + 1
    bot.register_next_step_handler(button_from_user, func_for_perevirka)


def func_for_perevirka(message):
    keyboard = types.ReplyKeyboardMarkup(False)
    global cor_ans
    if message.text == dct[qes][3]:
        cor_ans = cor_ans + 1
        bot.send_photo(message.chat.id, open('TRUE.jpg', 'rb'))
        bot.send_message(message.chat.id, text=f'Відповіть {dct[qes][3]} правильна! ✅')
        func_for_random(message)
    else:
        bot.send_photo(message.chat.id, open('ERROR.jpg', 'rb'))
        bot.send_message(message.chat.id, text=f'Відповіть {message.text} неправильна! ❌\n'
                                               f'Правильна відповідь: {dct[qes][3]}')
        func_for_random(message)


def func_the_end(message):
    if cor_ans < 5:
        lvl = 'A1'
    elif cor_ans >= 5 and cor_ans <= 9:
        lvl = 'A2'
    elif cor_ans >= 10 and cor_ans <= 14:
        lvl = 'B1'
    elif cor_ans >= 15 and cor_ans <= 19:
        lvl = 'B2'
    elif cor_ans == 20:
        lvl = 'C1'
    bot.send_message(message.chat.id, text=f'\nПравильних відповідей: {cor_ans} з {num}\n'
                                           f'Ваш рівень: {lvl}')
    main_func(message)

# -----------------------------------------------------------------sport

def sport(message):
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=2)
    button1 = types.KeyboardButton(text='Тренування')
    button2 = types.KeyboardButton(text='Пробіжка')
    buttons.add(button1, button2,)
    button_from_user = bot.send_message(message.chat.id, text='Обирай активність🏃',
                                        reply_markup=buttons)
    bot.register_next_step_handler(button_from_user, func_for_perevirka_training_or_run)


def func_for_perevirka_training_or_run(message):
    if message.text == 'Тренування':

        func_for_sport_training(message)
    elif message.text == 'Пробіжка':
        func_for_sport_run(message)


def func_for_sport_training(message):
    global numb_vprava
    numb_vprava = 1
    print('Тренування')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=3)
    button1 = types.KeyboardButton(text='Тренування на мязи рук')
    button2 = types.KeyboardButton(text='Тренування на мязи пресу')
    button3 = types.KeyboardButton(text='Тренування на мязи ніг')
    buttons.add(button1, button2, button3)
    button_from_user = bot.send_message(message.chat.id, text='Оберай тренування',
                                        reply_markup=buttons)

    bot.register_next_step_handler(button_from_user, func_for_perevirka_training)


def func_for_perevirka_training(message):
    global numb_vpr
    numb_vpr = 0
    if message.text == 'Тренування на мязи рук':
        global list_hand
        list_hand = []
        with open('vprava_on_hand.txt', 'r', encoding="utf-8") as file:
            for i in file.readlines():
                list_hand.append(i.strip('\n'))
        func_for_trenuvannya_na_myazi_ruk(message)

    elif message.text == 'Тренування на мязи пресу':
        global list_press
        list_press = []
        with open('vprava_on_press.txt', 'r', encoding="utf-8") as file:
            for i in file.readlines():
                list_press.append(i.strip('\n'))
        func_for_trenuvannya_na_myazi_presu(message)

    elif message.text == 'Тренування на мязи ніг':
        global list_legs
        list_legs = []
        with open('vprava_on_legs.txt', 'r', encoding="utf-8") as file:
            for i in file.readlines():
                list_legs.append(i.strip('\n'))
        func_for_trenuvannya_na_myazi_nih(message)


def func_for_trenuvannya_na_myazi_ruk(message):
    global send
    global numb_vprava
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=False,
                                        row_width=5)
    button1 = types.KeyboardButton(text=f'Next')
    buttons.add(button1)
    button_from_user = bot.send_message(message.chat.id, text=f'Вправа №{numb_vpr+1}\n{list_hand[numb_vpr]}',
                                        reply_markup=buttons)
    bot.send_photo(message.chat.id, open(f'{numb_vprava}.jpg', 'rb'))
    numb_vprava = numb_vprava + 1
    send = 1
    bot.register_next_step_handler(button_from_user, func_for_next_step)


def func_for_trenuvannya_na_myazi_presu(message):
    global send
    global numb_vprava
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=False,
                                        row_width=5)
    button1 = types.KeyboardButton(text=f'Next')
    buttons.add(button1)
    button_from_user = bot.send_message(message.chat.id, text=f'Вправа №{numb_vpr + 1}\n{list_press[numb_vpr]}',

                                        reply_markup=buttons)
    bot.send_photo(message.chat.id, open(f'{numb_vprava}p.jpg', 'rb'))
    numb_vprava = numb_vprava + 1
    send = 2
    bot.register_next_step_handler(button_from_user, func_for_next_step)


def func_for_trenuvannya_na_myazi_nih(message):
    global numb_vprava
    global send
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=False,
                                        row_width=1)
    bot.send_photo(message.chat.id, open(f'{numb_vprava}.jpg', 'rb'))
    button1 = types.KeyboardButton(text=f'Next')
    buttons.add(button1)
    button_from_user = bot.send_message(message.chat.id, text=f'Вправа №{numb_vpr + 1}\n{list_legs[numb_vpr]}',
                                        reply_markup=buttons)
    numb_vprava = numb_vprava + 1
    send = 3
    bot.register_next_step_handler(button_from_user, func_for_next_step)


def func_for_next_step(message):
    global numb_vpr
    if numb_vpr == 3:
        func_for_end(message)
    elif message.text == 'Next':
        numb_vpr += 1
        if send == 1:
            func_for_trenuvannya_na_myazi_ruk(message)
        elif send == 2:
            func_for_trenuvannya_na_myazi_presu(message)
        elif send == 3:
            func_for_trenuvannya_na_myazi_nih(message)


def func_for_end(message):

    bot.send_message(message.chat.id, text=f'Ви прийшли тренування')
    strat(message)


def func_for_sport_run(message):
    print('Пробіжка')
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=3)
    button1 = types.KeyboardButton(text='Знайти напарника')
    button2 = types.KeyboardButton(text='Запланувати пробіжку')

    buttons.add(button1, button2)
    button_from_user = bot.send_message(message.chat.id, text='Виберіть',
                                        reply_markup=buttons)

    bot.register_next_step_handler(button_from_user, func_for_serch)


def func_for_serch(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Search", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(message.chat.id, "Дозвольте локацію", reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def location(message):
    global dct
    global dct_new
    global a
    global lst_name
    global my_location
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=1)
    latitude = message.location.latitude
    longitude = message.location.longitude
    user_name = message.from_user.username
    print(user_name)

    my_location = (latitude, longitude)
    dct[user_name] = my_location
    a = a + 1
    buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                        row_width=2)
    button1 = types.KeyboardButton(text='Список учасників')
    button2 = types.KeyboardButton(text='Вихід')
    buttons.add(button1, button2)

    button_from_user = bot.send_message(message.chat.id, text='Всі учаснки будуть вам доступні',
                                        reply_markup=buttons)
    bot.register_next_step_handler(button_from_user, func_for_ex)

def func_for_ex(message):
    global distance
    if message.text == 'Список учасників':
        for i in dct.keys():
            print(i)
            distance = f'{i} - {(geopy.distance.distance(my_location, dct[i]).km)}km'
            bot.send_message(message.chat.id, text=f'Список учасників:\n{distance}',)

        buttons = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            row_width=1)
        button1 = types.KeyboardButton(text='Вихід')
        buttons.add(button1)
        button_from_user = bot.send_message(message.chat.id, text='Вихід)',
                                            reply_markup=buttons)
        bot.register_next_step_handler(button_from_user, func_for_ex)

    elif message.text == 'Вихід':
        strat(message)

def func_for_notification(message):
    print('notification')





if __name__ == '__main__':
    bot.polling(none_stop=True)
