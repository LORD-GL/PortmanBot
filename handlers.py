# file with handlers
def bot_start(bot, App):
    App.init_keyboards()
    # Start
    @bot.message_handler(commands=['start'])
    def start_menu(message):
        grettings = """ Приветствие! """
        bot.send_message(message.chat.id, grettings, reply_markup = App.main_keyboard)

    # Inf
    @bot.message_handler(func = lambda message: message.text == "Информация")
    def help(message):
        price = """
Обычный - 100 руб
С куратором - 200 руб 
VIP - 300 руб
                """
        bot.send_message(message.chat.id, price, reply_markup = App.connect_buy_keyboard)

    # pay
    @bot.message_handler(func = lambda message: message.text == "Оплата" or message.text == "Приобрести курс")
    def pay(message):
        requisites = """ 
MoноБанк   1111111111111
ПриватБанк 1111111111111"""
        bot.send_message(message.chat.id, requisites, reply_markup = App.end_keyboard)

    # admin help
    @bot.message_handler(func = lambda message: message.text == "Связь с админом")
    def adm_help(message):
        bot.send_message(message.chat.id, "Наш админ: @kidkate_moto", reply_markup = App.end_keyboard)