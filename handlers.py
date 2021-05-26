# file with handlers
def bot_start(bot, App):
    App.init_keyboards()
    # Start
    @bot.message_handler(commands=['start'])
    @bot.message_handler(func = lambda message: message.text == "Начало")
    def start_menu(message):
        grettings = """
Привет малых , тебя приветствует бот по
экспертным продуктам от Алисы Портман 🧠
    
Выбери, что тебя интересует 👇🏻
            """
        bot.send_message(message.chat.id, grettings, reply_markup = App.main_keyboard)

    @bot.message_handler(func = lambda message: message.text == "Пиробрести гайд по визуалу")
    def guide(message):
        bot.send_message(message.chat.id, "Свяжитесь с нашим админом @kidkate_moto", reply_markup = App.end_keyboard)

    ############### Inf ###############
    ######## Inf mode
    @bot.message_handler(func = lambda message: message.text == "Приобрести менторство")
    def help(message):
        bot.send_message(message.chat.id, "Выберите тип менторства", reply_markup = App.mode_keyboard)
    ### mode own ###
    @bot.message_handler(func = lambda message: message.text == "Менторство для личного блога")
    def own_usage(message):
        price = """
Я все сам 3490 руб/1290 грн
С куратором было бы гуд 8990 руб/3350 грн
Хочу пендель от Алисы 15 990 руб/5950 грн
        """
        bot.send_message(message.chat.id, price, reply_markup = App.own_callbck_keyboard)

    @bot.callback_query_handler(func = lambda message: message.data == "3490")
    def p_3490(message):
        serv = """
В этот тариф  входит:

🧠 8 видеоуроков от Алисы Портман.
        """
        bot.send_message(message.from_user.id, serv, reply_markup = App.connect_buy_keyboard)

    @bot.callback_query_handler(func = lambda message: message.data == "8990")
    def p_7990(message):
        serv = """
В этот тариф  входит:

🧠8 видеоуроков от Алисы Портман 
🧠шпаргалки и домашки
🧠обратная связь от куратора 
🧠1 групповой созвон с Алисой Портман 
        """
        bot.send_message(message.from_user.id, serv, reply_markup = App.connect_buy_keyboard)

    @bot.callback_query_handler(func = lambda message: message.data == "15 990")
    def p_13990(message):
        serv = """
В этот тариф  входит:

🧠10 видеоуроков 
🧠шпаргалки и домашки
🧠обратная связь от Алисы Портман
🧠2 личных созвона с Алисой Портман
        """
        bot.send_message(message.from_user.id, serv, reply_markup = App.connect_buy_keyboard)

    ### mode manage #######################
    @bot.message_handler(func = lambda message: message.text == "Менторство для менеджеров")
    def mng_usage(message):
        price = """ 
Я все сам 3990 руб/1490 грн
С куратором было бы гуд 9990 руб/3710 грн 
Хочу пендель от Алисы 16 990 руб/6 300 грн
"""
        bot.send_message(message.chat.id, price, reply_markup = App.mng_callbck_keyboard)

    @bot.callback_query_handler(func = lambda message: message.data == "3990")
    def p_3990(message):
        serv = """
В этот тариф  входит:

🧠 7 видеоуроков от Алисы Портман.
        """
        bot.send_message(message.from_user.id, serv, reply_markup = App.connect_buy_keyboard)

    @bot.callback_query_handler(func = lambda message: message.data == "9990")
    def p_8990(message):
        serv = """
В этот тариф  входит:

🧠7 видеоуроков от Алисы Портман 
🧠шпаргалки и домашки
🧠обратная связь от куратора 
🧠1 групповой созвон с Алисой Портман  
        """
        bot.send_message(message.from_user.id, serv, reply_markup = App.connect_buy_keyboard)

    @bot.callback_query_handler(func = lambda message: message.data == "16 990")
    def p_14990(message):
        serv = """
В этот тариф  входит:

🧠9 видеоуроков 
🧠шпаргалки и домашки
🧠обратная связь от Алисы Портман
🧠2 личных созвона с Алисой Портман
        """
        bot.send_message(message.from_user.id, serv, reply_markup = App.connect_buy_keyboard)

    ###### pay
    @bot.message_handler(func = lambda message: message.text == "Оплата" or message.text == "Приобрести курс")
    def pay(message):
        requisites = """ Реквизиты для оплаты:
5363 5420 1222 1595
Saliukova Alina 
Банк: Приватбанк. 
Страна: Украина. 
Сделайте скриншот и скиньте админу.
                """
        bot.send_message(message.chat.id, requisites, reply_markup = App.end_keyboard)

    # admin help
    @bot.message_handler(func = lambda message: message.text == "Связь с админом")
    def adm_help(message):
        bot.send_message(message.chat.id, "Наш админ: @portmanalisa", reply_markup = App.end_keyboard)