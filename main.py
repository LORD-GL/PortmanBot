# -*- coding: utf-8 -*-
"""
    Maded by LeLord
    ver. 0.1
# """

from funcs import App

app = App()

from handlers import bot_start as main

main(app.bot, app)

app.bot.polling(none_stop = True)