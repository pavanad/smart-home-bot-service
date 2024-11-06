import logging
import os
import sys

from dotenv import load_dotenv

load_dotenv()


def enable_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s (%(name)s) %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)


# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Grace Service
GRACE_SERVICE_URL = os.getenv("GRACE_SERVICE_URL")
