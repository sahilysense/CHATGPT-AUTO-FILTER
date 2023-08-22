import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 26936024  # Replace with your API ID
API_HASH = '5b44fda5c2576ee1999bf3af8288e4e2'  # Replace with your API HASH
BOT_TOKEN = "6604579831:AAGFo_9Z8qAcNT9ohNuQPuBkqccMuGT6XPs"

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/b806ad314d0c415571bde.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '2001653136').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '2001653136').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = '1977133520'
auth_grp = '936698840'
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = "mongodb+srv://Popindiaxbot:sahil@8989@cluster0.9uhus0k.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = 'Telegram_files'

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '1977163469'))
SUPPORT_CHAT = 'search_zone_support'
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = "ɴᴀᴍᴇ: <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [GreyMatter's Bot](https://t.me/greymatter_bots)</b>"
BATCH_FILE_CAPTION = "ɴᴀᴍᴇ: <code>{file_name}</code> \n\nᴊᴏɪɴ ɴᴏᴡ: [GreyMatter's Bot](https://t.me/greymatter_bots)</b>"
IMDB_TEMPLATE = "🧿 ᴛɪᴛᴛʟᴇ :  {title} \n🌟 ʀᴀᴛɪɴɢ : {rating} \n🎭 ɢᴇɴʀᴇ : {genres} \n📆 ʀᴇʟᴇᴀsᴇ : {year} \n⏰ ᴅᴜʀᴀᴛɪᴏɴ : {runtime} \n🎙️ʟᴀɴɢᴜᴀɢᴇ : {languages} \n🔖 sʜᴏʀᴛ : {plot} \n★ ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @GreyMatter_Bots"
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Customized Configurations are:\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing IMDb details for your queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending a file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and file size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled, filename and file size will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be sent along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of files will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, the plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, the bot will be suggesting related movies if a movie is not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, a long list will be shortened to the first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "The full list of casts and crew will be shown in the IMDb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDb template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##
    
# URL Shortener
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', 'omegalinks.in')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '7570653688b21e9eba68303b57b83e6ae982cc39')

