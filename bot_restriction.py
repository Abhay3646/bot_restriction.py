import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your bot token as a secret in the GitHub repository settings
TOKEN = os.environ.get('BOT_TOKEN')

# Set the restriction duration in seconds (6 days)
RESTRICTION_DURATION = 6 * 24 * 60 * 60

def restrict_new_member(update: Update, context: CallbackContext) -> None:
    user_id = update.message.new_chat_members[0].id
    chat_id = update.message.chat_id

    context.bot.restrict_chat_member(chat_id, user_id, can_send_messages=False, until_date=update.message.date + RESTRICTION_DURATION)

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, restrict_new_member))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
