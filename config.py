#(©)t.me/CodeFlix_Bots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", ":7155863501:AAHJ3NG4uTJIp5VZy7AlPCznSW0vQNdp3pg")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29862293"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ed2b66047d283a53433ffb4a9ef23464")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002256160837"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "JBLJAY")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7132799559"))

#Port
PORT = os.environ.get("PORT", "8018")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://panchalishanibigbigpvtltd:oZtI0tHJw1yWfYI4@cluster0.ee5qz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharingbybackbenc")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001911546743"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002240500177"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}</b>\n\nmuth marna band kr de dusro ko sex krte dekh muth marne maja aata kya?? cuck ho? eww bhai imagine tumhara brain itna fucked up ho chuka hai ki tum dusro ko sex krte dekh maja ata sad bhai ye sab band kr do @brainsaga if you want bot like this </a></b>")
try:
    ADMINS=[7132799559]
    for x in (os.environ.get("ADMINS", "7132799559").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello {first}!\nTo access these files you have to join our channel first.\nPlease subscribe to our channels through the buttons below and then tap on try again to get your files.\nThank You ❤️")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>By @JBLTOXIC</a>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(7132799559)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
