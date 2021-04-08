import telebot
# functions class file
class App():
    def __init__(self):    
        from conf import Conf
        self.conf = Conf()
        self.bot = telebot.TeleBot(self.conf.HTTP_API)

    def init_keyboards(self):
        self.main_menu_init()
        self.help_menu_init()
        self.end_menu_init()

    def main_menu_init(self):
        self.main_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        self.main_keyboard.row('Приобрести курс', 'Информация')

    def help_menu_init(self):
        self.connect_buy_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        self.connect_buy_keyboard.row('Связь с админом', 'Оплата')

    def end_menu_init(self):
        self.end_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        self.end_keyboard.row('Связь с админом', '/start')