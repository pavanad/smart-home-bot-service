import os

from dotenv import load_dotenv

load_dotenv()


def main():
    token = os.getenv("TELEGRAM_TOKEN", "")


if __name__ == "__main__":
    main()
