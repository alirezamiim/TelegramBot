from telegram.ext import (Updater , CommandHandler , ConversationHandler , MessageHandler,
                          CallbackContext)
from telegram.ext import ApplicationBuilder


import logging
from telegram import Update ,ReplyKeyboardMarkup
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def Profile_Handler(major=''):
    majors={'economics':['kasra','mahla'],'telecommunication':['mahsa'],'electronics':['alireza'],
            'bio-informatic':['Amir']}
    return majors[major]


def start_handler(update,context:CallbackContext):
    WELCOME_NOTE = 'Welcome to this bot.\nبه این ربات خوش آمدید.\nیک کشور رو انتخاب کنید:'
    update.message.reply_text(text= WELCOME_NOTE,reply_markup=add_country_key())

    
def add_country_key():
    keyboards = [['US','Canda'],['UK','Netherland','Italy'],['China','India']] 
    return ReplyKeyboardMarkup(keyboard=keyboards,resize_keyboard=True,one_time_keyboard=True)
    
def help_handler(update:Update):
    HELP_NOTE = '''اگر در استفاده از ربات به مشکل خوردید، لطفا آن را به آی دی @alirezamiim گزارش دهید.
    ممنونم که به ما در بهبود این ربات کمک میکنید.
                '''
    update.message.reply_text('no need for help')

    
def country_hanler(update:Update,context:CallbackContext):
    country = update.message.text
    update.message.reply_text('You have Entered '+country)
    if country in ['UK','US','China','Canada','Netherland','Italy','India']: 
        update.message.reply_text('Please Enter your Major:')
        return 0
        
        
    
def enter_message_handler(update:Update,context :CallbackContext):
    major = update.message.text
    update.message.reply_text('You entered '+major+' as your major')
    major = major.lower()
    profiles = Profile_Handler(major=major)
    index = 1
    for profile in profiles:
        
        update.message.reply_text(str(index)+'. is '+profile)
        index += 1
    
    
    
    
    
    
    

if __name__ == '__main__':

    pass
    

