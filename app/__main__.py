import io
import logging
import os

from callbacks.text_message import text_message
from callbacks.voice_message import voice_message
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

load_dotenv()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


def main() -> None:
    token = os.getenv("TELEGRAM_TOKEN", "")

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
