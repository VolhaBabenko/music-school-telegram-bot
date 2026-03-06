import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
DB_DSN = os.getenv('DB_DSN', 'postgresql://localhost/music_bot')
ADMIN_CHAT_ID = int(os.getenv('ADMIN_CHAT_ID', '0'))
