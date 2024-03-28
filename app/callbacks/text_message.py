import logging

from services.grace import grace_service_invoke
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"Received text: {update.message.text}")
    response = grace_service_invoke(update.message.text)
    await update.message.reply_text(response)
