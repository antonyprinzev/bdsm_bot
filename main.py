# telebot is simple lib to use Telegram-bot API
import telebot
from telebot import types

API_TOKEN = '7465800268:AAHDNk06YQGzRvEJEth4PuLmZlrsfSTjw9M'

bot = telebot.TeleBot(API_TOKEN)

sasha = bot.set_chat_menu_button()

# автоматически применяет функцию handle от telebot после использования функции send_welcome
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, '''\
    Привет!
    
    Этот бот будет помогать тебе достигать результатов эффективнее и дисциплинированнее. 
    
    Для того, чтобы начать - напиши любое сообщение"\
    ''')

    bot.register_next_step_handler(message, prank)

def prank(message):

    keyboard = telebot.types.InlineKeyboardMarkup() # объявляем клаву
    key_yes = telebot.types.InlineKeyboardButton(text='да', callback_data="yes")
    key_no = telebot.types.InlineKeyboardButton(text='нет', callback_data="no")
    keyboard.add(key_yes)
    keyboard.add(key_no)

    bot.send_message(message.chat.id, text="ты чё, хуила, Измайлов что ли?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call == 'да':
        bot.send_message(call.message.chat.id, text='''Вот ты и попался блять!
        ……………………………....…………._¸„„„„_
……………………....…………...„--~*'¯…….'/
………….…....………………… („-~~--„¸_….,/ì'Ì
……....………….………….¸„-^"¯ : : : : :¸-¯"¯/'
………....……………¸„„-^"¯ : : : : : : : '/¸„„,-"
**¯¯¯'^^~-„„„----~^*'"¯ : : : : : : : : : :¸-"
.:.:.:.:.„-^" : : : : : : : : : : : : : : : : :„-"
:.:.:.:.:.:.:.:.:.:.: : : : : : : : : : ¸„-^¯
.::.:.:.:.:.:.:.:. : : : : : : : ¸„„-^¯
:.' : : '/ : : : : : : : ;¸„„-~"
:.:.:: :"-„""***/*'ì¸'¯
:.': : : : :"-„ : : :"/
.:.:.: : : : :" : : : : /,
:.: : : : : : : : : : : : 'Ì
: : : : : : :, : : : : : :/
"-„_::::_„-*__„„~"
    ''')

    else:
        keyboard = telebot.types.InlineKeyboardMarkup()
        yes = telebot.types.InlineKeyboardButton(text='Да', callback_data="yes")
        no = telebot.types.InlineKeyboardButton(text='Нет', callback_data="no")
        keyboard.add(yes, no)

        bot.send_message(call.message.chat.id, text="Ты меня наебать решил?", reply_markup=keyboard)

        bot.register_next_step_handler(call.message, prank)



bot.infinity_polling()

