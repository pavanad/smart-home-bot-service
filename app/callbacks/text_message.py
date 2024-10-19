import logging

from services.grace import grace_service_invoke
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"Received text: {update.message.text}")
    first_name = update.message.chat.first_name
    message = f"My name is {first_name}! {update.message.text}"
    response = grace_service_invoke(message, update.message.chat_id)
    await update.message.reply_text(response)
