import constants as keys
from telegram.ext import * 
import datetime as datetime
from flat import Flats

print("Bot started...")

def start_command(update, context):
    update.message.reply_text('Napisz nazwe dzielnicy zeby zaczac')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)


def callback_alarm(context):
    FlatOchota = Flats("Ochota")
    FlatWlochy = Flats("Wlochy")
    FlatMokotow = Flats("Mokotow")
    context.bot.send_message(context.job.context, text=FlatWlochy.numberOfFLats())
    context.bot.send_message(context.job.context, text=FlatOchota.numberOfFLats())
    context.bot.send_message(context.job.context, text=FlatMokotow.numberOfFLats())

#def time(update, context):
 #   context.job_queue.run_repeating(sayhi, 20, context=update.message.chat_id)



def callback_timer(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                      text='Starting!')
    context.job_queue.run_repeating(callback_alarm, 1200, context=update.message.chat_id)

def stop_timer(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                      text='Stoped!')
    context.job_queue.stop()
 


def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', callback_timer))
    dp.add_handler(CommandHandler('stop', stop_timer))

    
    updater.start_polling()
    updater.idle()

main()