import os
from dotenv import load_dotenv

load_dotenv()


TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
OPENAI_TOKEN = os.environ.get("OPENAI_TOKEN")
