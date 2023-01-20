# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [YouTube-Bot](https://github.com/sanila2007/YouTube_bot_telegram)

# Read GNU General Public License v3.0: https://github.com/sanila2007/YouTube_bot_telegram/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I am doing these things for free and open source
# Star, fork, enjoy!

import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", 21569673))
    API_HASH = os.environ.get("API_HASH","1ba68f53204b8add14973b7c7fdda399")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","5895581615:AAFXUNzqSqGTwitPaXfW4wpYDT4lpjZMFKs")
