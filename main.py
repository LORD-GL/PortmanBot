# -*- coding: utf-8 -*-
"""
    -------------------
    | Maded by LeLord |
    -------------------
    ver. 1.0 04.11.2021
    https://t.me/LORD_GL 
# """

from funcs import App

app = App()

from handlers import bot_start as main

main(app.bot, app)

app.bot.polling(none_stop = True)