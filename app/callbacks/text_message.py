from telegram import Update
from telegram.ext import ContextTypes


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # TODO: implement calling Grace Service
    await update.message.reply_text(update.message.text)
