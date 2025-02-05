# PTAF subnet to regex telegram bot

This is a Telegram bot that converts IPv4 subnets to regular expressions. It allows you to input an IPv4 subnet, and the bot will return the corresponding regular expression (regex) to match the network.

## Features

- Converts IPv4 subnets into regex patterns.
- Provides visual feedback using emoji:
    - ✅ for correct subnets
    - ⚠️ for potential issues with the subnet
    - ❌ for errors when the input is invalid
- Responds to multiple subnet inputs on separate lines.

## How to Use

1. **Start the Bot:**
    - Send `/start` to the bot, and it will reply with a welcome message and instructions.

2. **Input a Subnet:**
    - Send an IPv4 subnet to the bot (e.g., `192.168.1.0/24`).
    - The bot will reply with the corresponding regex.
    - If the subnet is invalid or malformed, the bot will return an error message.

3. **Multiple Inputs:**
    - You can send multiple subnets at once, each on a new line.
    - The bot will respond with the regex for each subnet.

## Requirements

To run this bot, you'll need to have the following:

- Python 3.x
- `pip` for installing dependencies

### Python Libraries

- `python-telegram-bot` – For interacting with Telegram's Bot API
- `ipaddress` – For working with IP networks
- `dotenv` – To manage environment variables
- `logging` – For logging bot activity

### Setup Instructions

1. Clone or download the repository.

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt


### To run

1. Create .env file with TELEGRAM_BOT_TOKEN value

2. Run bot.py 
