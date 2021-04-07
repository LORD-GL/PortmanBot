# file with handlers
def bot_start(bot, App):
    App.init_keyboards()
    # Start menu
    @bot.message_handler(commands=['start'])
    def start_menu(message):
        grettings = """ Приветствие! """
        bot.send_message(message.chat.id, grettings, reply_markup = App.main_keyboard)

    # Inf menu
    @bot.message_handler(func = lambda message: message.text == "Информация")
    def Help(message):
        price = """
Обычный - 100 руб
С куратором - 200 руб 
VIP - 300 руб
                """
        bot.send_message(message.chat.id, price, reply_markup = App.connect_buy_keyboard)