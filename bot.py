import subprocess
from telegram import Update

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '7034879083:AAHK85BoLe8Oq_xCdW9HrYBJq8mhTQSphJM'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Пожалуйста, введите video_id:')

def handle_text(update: Update, context: CallbackContext) -> None:
    video_id = update.message.text

    with open('video_id.txt', 'w') as file:
        file.write(video_id)
    # Запускаем basedOn.py с переданным video_id => Bugkill: w/o video_id ||  pip install google-api-python-client -t ./
    subprocess.run(['python', 'basedOn.py'])

    # Отправляем пользователю полученный CSV-файл
    with open('youtuberesults.csv', 'rb') as file:
        update.message.reply_document(document=file)

def main() -> None:
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
