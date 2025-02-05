"""
  _____ _______       ______                                       _        _       _
 |  __ \__   __|/\   |  ____|                                     | |      | |     | |
 | |__) | | |  /  \  | |__     _ __ ___  __ _  _____  ___ __   ___| |_ __ _| |_ ___| |
 |  ___/  | | / /\ \ |  __|   | '__/ _ \/ _` |/ _ \ \/ / '_ \ / _ \ __/ _` | __/ _ \ |
 | |      | |/ ____ \| |      | | |  __/ (_| |  __/>  <| | | |  __/ || (_| | ||  __/ |
 |_|      |_/_/    \_\_|      |_|  \___|\__, |\___/_/\_\_| |_|\___|\__\__,_|\__\___|_|
                                         __/ |
                                        |___/
"""

import os
import dotenv
import logging
import telebot
import ipaddress

from ipv4_to_regex import ipv4_to_regex, test_it

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

dotenv.load_dotenv()
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)
logger = logging.getLogger(__name__)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.info(f"Received /start command from {message.from_user.username}")
    bot.reply_to(message, "отправь подсеть - получи регулярку. все просто")


@bot.message_handler(func=lambda message: True)
def convert_to_regex(message):
    messages = []
    for line in message.text.splitlines():
        try:
            net = ipaddress.IPv4Network(line, strict=False)
            regex = ipv4_to_regex(net)
            prefix = '✅' if line == str(net) else '⚠️'
            messages.append(f'{prefix} {regex}')
        except Exception as e:
            messages.append(f'❌ апшибка: {str(e)}')

    bot.reply_to(message, '\n'.join(messages))


if __name__ == '__main__':
    logger.info("Bot started...")
    bot.polling(none_stop=True)

