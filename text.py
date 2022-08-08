# import telebot
# from telebot import types
# import geopy.distance
# bot = telebot.TeleBot('2084950457:AAFHmbs-Sn6H3plEe0bh0A2YZ1kr7G04YVA')
#
# @bot.message_handler(commands=["start"])
# def start (message):
#     keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
#     button_geo = types.KeyboardButton(text="Search", request_location=True)
#     keyboard.add(button_geo)
#     bot.send_message(message.chat.id, "Поділись місцерозташуванням", reply_markup=keyboard)
#
# @bot.message_handler(content_types=['location'])
# def location(message):
#     latitude = message.location.latitude
#     longitude = message.location.longitude
#
#
#     coords_1 = (latitude, longitude)
#     coords_2 = (49.302528, 23.814547)
#
#
#
#
#     print(geopy.distance.distance(coords_1, coords_2).km)
#
#
#
# bot.polling(none_stop = True)
dct = {1:'21'}
dct.update({2:3232})

print(dct)

while True:
    a = int(input())
    b = int(input())
    dct.update({a:b})
    print(dct )
