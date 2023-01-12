import telebot #import the telebot library which allows to interact with the Telegram API
import time   #import the time library to measure the elapsed time

bot_token = 'YOUR_BOT_TOKEN' #The token for your bot, provided by the BotFather
bot = telebot.TeleBot(bot_token)   #create the bot object using the bot_token

# Handling updates from Telegram
@bot.message_handler(commands=['start'])  #set the function to handle the '/start' command
def start(message):
    bot.send_message(message.chat.id, "Welcome! Type /help for more information.")  #send a welcome message

@bot.message_handler(commands=['help']) #set the function to handle the '/help' command
def help(message):
    bot.send_message(message.chat.id, "I can provide information about XYZ. Type /info for more information.")  #send a help message

@bot.message_handler(commands=['info']) #set the function to handle the '/info' command
def info(message):
    bot.send_message(message.chat.id, "XYZ is a platform for ABC.")  #send an info message

start_time = time.time() #save the current time
bot.polling()  #handles updates from Telegram
while True:  #loop infinitely
    if time.time() - start_time > 180: #check if 3 minutes have passed
        break   #break the loop and stop the script
