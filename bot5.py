import telebot # importamos la libreria de telebot
bot = telebot.TeleBot('1903524960:AAGyfpkrZ3w_il8PJvpOWHQCr_FdqVa8x_c') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()
@bot.message_handler(commands=['hola']) #definimos el comando
def hola(mensaje):
    bot.reply_to(mensaje, "Hola")
    print("Mandaron hola")
@bot.message_handler(commands=['foto', 'photo'])
def conversion(mensaje):
    bot.send_chat_action(id, 'typing')
    photo = open('photo.jpg', 'rb')
    bot.send_photo(id, photo)  


@bot.message_handler(commands=['video'])
def documento(mensaje):
    bot.send_chat_action(id, 'typing')
    video = open('video.MP4', 'rb')
    bot.send_video(id, video)


bot.polling()
