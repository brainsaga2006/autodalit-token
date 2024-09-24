#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "0")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29862293"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ed2b66047d283a53433ffb4a9ef23464")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002332524290"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7132799559"))

#Port
PORT = os.environ.get("PORT", "1112")

#Database 
DB_URI = "mongodb+srv://Backbenchersnevakakms:PLs5YvLbUYWRJXk8@cluster0.u3mmn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "shortxlinks.com/")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "ed1a4fc18ddd4e915ebb8468a96ae3bb39752adf")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE',50400 )) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002327738776"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[7132799559]
    for x in (os.environ.get("ADMINS", "7132799559").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\https://t.me/BackbenchersBackupOnly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "This video/Photo/anything is available on the internet. We @BackbenchersBackupOnly or its subsidiary channel doesn't produce any of them.")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

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