# file with handlers
def bot_start(bot, App):
    App.init_keyboards()
    # Start
    @bot.message_handler(commands=['start'])
    def start_menu(message):
        grettings = """
Привет малых , тебя приветствует бот по
экспертным продуктам от Алисы Портман 🧠
    
Выбери, что тебя интересует 👇🏻
            """
        bot.send_message(message.chat.id, grettings, reply_markup = App.main_keyboard)

    ### Inf ###
    # Inf mode
    @bot.message_handler(func = lambda message: message.text == "Приобрести менторство")
    def help(message):
        bot.send_message(message.chat.id, "Выберите тип менторства", reply_markup = App.mode_keyboard)
    # mode own
    @bot.message_handler(func = lambda message: message.text == "Менторство для личного блога")
    def own_usage(message):
        price = """

        """
        bot.send_message(message.chat.id, )

    # pay
    @bot.message_handler(func = lambda message: message.text == "Оплата" or message.text == "Приобрести курс")
    def pay(message):
        requisites = """ 
MoноБанк   1111111111111
ПриватБанк 1111111111111
                """
        bot.send_message(message.chat.id, requisites, reply_markup = App.end_keyboard)

    # admin help
    @bot.message_handler(func = lambda message: message.text == "Связь с админом")
    def adm_help(message):
        bot.send_message(message.chat.id, "Наш админ: @kidkate_moto", reply_markup = App.end_keyboard)