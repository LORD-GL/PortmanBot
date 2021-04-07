# functions file
from conf import Conf
from telebot import TeleBot

bot, conf = None, None

def init():
    global conf, bot
    conf = Conf()
    bot = TeleBot(conf.HTTP_API)