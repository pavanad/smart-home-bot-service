import logging
import os


def enable_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s (%(name)s) %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        filename="logs/bot_service.log",
        filemode="a",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)


# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
