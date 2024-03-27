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


def get_token() -> str:
    return os.getenv("TELEGRAM_TOKEN")
