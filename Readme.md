# Daily Horoscope Message Sender Telegram Bot

This Python script allows you to send a Daily Horoscoy message to a personal chat or channel using a Telegram bot. It utilizes the `python-telegram-bot` library to interact with Telegram's API asynchronously.

## Features

- Sends a Horoscope messages to a personal chat or Telegram channel.
- Uses the Telegram Bot API to interact with Telegram.

## Requirements

- Python 3.7+
- Telegram Bot Token
- Python Libraries: 
  - `python-telegram-bot`
  - `python-dotenv`
  - `asyncio`

## Usages

1. **Clone the repository :**
   ```bash
   git clone https://github.com/santoshvandari/DailyHoroscopeUpdateTelegramBot.git
   cd DailyHoroscopeUpdateTelegramBot
    ```
2. **Set up a virtual environment (optional but recommended) :**
    ```bash
    python3 -m virtualenv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install dependencies :**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up the environment variables :**
    - Create a .env file in the root of the script by the following command:
    ```bash
    cp .env.example .env
    ```
    - You can obtain the [BOTAPIKEY](https://core.telegram.org/api/obtaining_api_id) by creating a bot via BotFather on Telegram.
    - To get your CHATID, start a conversation with your bot and use the provided script to get the chat ID.

5. **Run the Script :**
     ```bash
    python3 main.py
     ```

## Contributing
We welcome contributions! If you'd like to contribute to this Mero Share IPO Filler Script, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this Script.

## License
This project is licensed under the MIT [License](LICENSE).