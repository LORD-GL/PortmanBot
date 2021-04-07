# file with handlers
from funcs import *

# Start menu
@bot.message_handler(commands=['start'])
def start_menu(message):
    bot.send_message(message.chat.id, "Hello!")