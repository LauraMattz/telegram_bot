import schedule   #import the schedule library
import time       #import the time library
import telebot    #import the telebot library which allows to interact with the Telegram API

bot_token = 'xxxxxx'   #The token for your bot, provided by the BotFather
bot = telebot.TeleBot(bot_token)   #create the bot object using the bot_token

chat_id = 'xxxx'   #The chat ID of the user or group you want to send the message to

msg = "Colocar msg aqui"   #The message to be sent

def job():   
    bot.send_message(chat_id, msg)  #function that sends the message
    schedule.cancel_job(job)   #cancel the job after running once.

schedule.every().day.at("08:00").do(job)   #schedule the job to run at 8 am every day

while True:
    schedule.run_pending()  # check if there are any scheduled jobs pending
    time.sleep(1)  # pause the script for 1 second before checking again
