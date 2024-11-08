import logging

from messages import ERROR_INVOKING_GRACE_SERVICE
from services.grace import grace_service_invoke
from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def text_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"Received text: {update.message.text}")
    first_name = update.message.chat.first_name
    message = f"Username is {first_name}! {update.message.text}"

    try:
        response = grace_service_invoke(message, update.message.chat_id)
    except Exception as e:
        logger.error(f"Error invoking grace service: {e}")
        response = ERROR_INVOKING_GRACE_SERVICE

    await update.message.reply_text(response)
