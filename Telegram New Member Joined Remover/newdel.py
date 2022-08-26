import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, filters, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

Bot_token = '################################'

async def join_chat_del(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.delete()

if __name__ == '__main__':
    application = ApplicationBuilder().token(Bot_token).concurrent_updates(True).build()
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, join_chat_del, block=False))

    application.run_polling()
