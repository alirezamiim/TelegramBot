import logging
from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)





def add_country_key():
    keyboards = [['US','Canda'],['UK','Netherland','Italy'],['China','India']] 
    return ReplyKeyboardMarkup(keyboard=keyboards,resize_keyboard=True,one_time_keyboard=True)


async def help_handler(update:Update,context: ContextTypes.DEFAULT_TYPE):
    HELP_NOTE = '''اگر در استفاده از ربات به مشکل خوردید، لطفا آن را به آی دی @alirezamiim گزارش دهید.
    ممنونم که به ما در بهبود این ربات کمک میکنید.
                '''
    await context.bot.send_message(chat_id = update.effective_chat.id,text = HELP_NOTE)

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    WELCOME_NOTE = 'Welcome to this bot.\nبه این ربات خوش آمدید.\nیک کشور رو انتخاب کنید:'
    # update.message.reply_text(text= WELCOME_NOTE,reply_markup=add_country_key())
    await context.bot.send_message(chat_id=update.effective_chat.id, text=WELCOME_NOTE,reply_markup=add_country_key())

if __name__ == '__main__':
    application = ApplicationBuilder().token('5621800537:AAFWqfR8OJdlxgkliJrpehnVogAMphzeggI').build()
    
    start_handler_object = CommandHandler('start', start_handler)
    help_handler_object  = CommandHandler('help',help_handler)
    
    application.add_handler(start_handler_object)
    application.add_handler(help_handler_object)
    
    application.run_polling()