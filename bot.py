import telebot
from config import TOKEN
from logic import get_class


bot = telebot.TeleBot(TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, """\
# здарова бродяга я лейтинант-бот, отправь мне картинку а я угадаю кто это (голубь, синица, бобер, трубкозуб) \
""")
    
    bot.send_message(message.chat.id, """\
# аижапышгупарышпгыпигшыпгры \
""")

@bot.message_handler(content_types =["photo"]) 
def send_animal(messege):
    file_info = bot.get_file(messege.photo[-1].file_id)
    file_name = file_info.file_path.split("/")[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    with open(file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    result = get_class(file_name)
    bot.send_message(messege.chat.id, result)



bot.infinity_polling()



