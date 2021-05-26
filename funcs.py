import telebot
from conf import Conf
# functions class file
class App():
    def __init__(self):    
        self.conf = Conf()
        self.bot = telebot.TeleBot(self.conf.HTTP_API)

    def init_keyboards(self):
        self.main_menu_init()
        self.help_menu_init()
        self.end_menu_init()
        self.mode_menu_init()
        self.own_callbck_init()
        self.mng_callbck_init()

    # d
    def main_menu_init(self):
        self.main_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        self.main_keyboard.row('Приобрести менторство', 'Пиробрести гайд по визуалу')
        self.main_keyboard.row('Связь с админом')

    def mode_menu_init(self):
        self.mode_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        self.mode_keyboard.row('Менторство для личного блога')
        self.mode_keyboard.row('Менторство для менеджеров')

    def help_menu_init(self):
        self.connect_buy_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        self.connect_buy_keyboard.row('Связь с админом', 'Оплата')

    def end_menu_init(self):
        self.end_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        self.end_keyboard.row('Связь с админом', 'Начало')

    def own_callbck_init(self):
        self.own_callbck_keyboard = telebot.types.InlineKeyboardMarkup()
        self.own_callbck_keyboard.row(
            telebot.types.InlineKeyboardButton("3490₽", callback_data = "3490"),
            telebot.types.InlineKeyboardButton("8990₽", callback_data = "8990"),
            telebot.types.InlineKeyboardButton("15 990₽", callback_data = "15 990")
        )

    def mng_callbck_init(self):
        self.mng_callbck_keyboard = telebot.types.InlineKeyboardMarkup()
        self.mng_callbck_keyboard.row(
            telebot.types.InlineKeyboardButton("3990₽", callback_data = "3990"),
            telebot.types.InlineKeyboardButton("9990₽", callback_data = "9990"),
            telebot.types.InlineKeyboardButton("16 990₽", callback_data = "16 990")
        )