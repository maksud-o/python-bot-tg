import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I will forward every text message you send!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = update.effective_chat.id
    await context.bot.forward_message(chat_id=id, from_chat_id=id, message_id=update.message.id)

if __name__ == '__main__':
    application = ApplicationBuilder().token('TOKEN').build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(echo_handler)
    application.add_handler(start_handler)

    application.run_polling()