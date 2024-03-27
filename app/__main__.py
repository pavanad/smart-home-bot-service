import logging

from callbacks.text_message import text_message
from callbacks.voice_message import voice_message
from config import enable_logging, get_token
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

load_dotenv()


def main() -> None:
    enable_logging()
    logger = logging.getLogger(__name__)
    logger.info("Initializing bot service")

    token = get_token()
    application = Application.builder().token(token).build()
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, text_message)
    )
    application.add_handler(
        MessageHandler(filters.VOICE & ~filters.COMMAND, voice_message)
    )
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
