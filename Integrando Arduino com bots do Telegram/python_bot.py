from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from python_serial import light_on, light_off

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Bem vind@ ao bot do ArduinoDay!!')

def set_light_on(bot, update):
    light_on()
    update.message.reply_text('O led está ligado!')
    
def set_light_off(bot, update):
    light_off()
    update.message.reply_text('O led está desligado!')

def help(bot, update):
    update.message.reply_text('Comando ainda não implementado!')


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater("585527278:AAFF5ab1E01yAP7UXr5voQIoeMhXfcth7oA")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("light_on", set_light_on))
    dp.add_handler(CommandHandler("light_off", set_light_off))

    dp.add_error_handler(error)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
