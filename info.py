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
API_ID = 5548284 int(environ['API_ID'])
API_HASH = aeeec9cdd07eaa92c9c32de4de7a920f environ['API_HASH']
BOT_TOKEN = 1748842379:AAEWq7raVXCyo1g2W5Nn-4hr2QM36Sbbq3Y environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = 300 int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = True bool(environ.get('USE_CAPTION_FILTER', False))
PICS = https://telegra.ph/file/bb022e175ef100dccbbe1.jpg (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

# Admins, Channels & Users
ADMINS = 1099546187 [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = -1001546142021 [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
auth_users = 1099546187 [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = -1001734126103 environ.get('AUTH_CHANNEL')
auth_grp = -1001328188417environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = mongodb+srv://A2links:A2links@cluster0.ht6yr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority environ.get('DATABASE_URI', "")
DATABASE_NAME = cluster 0 environ.get('DATABASE_NAME', "Rajappan")
COLLECTION_NAME = Telegram_files environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = -1001676000562 int(environ.get('LOG_CHANNEL', 0))
SUPPORT_CHAT = LinkZz_MBBS environ.get('SUPPORT_CHAT', 'TeamEvamaria')
P_TTI_SHOW_OFF = True is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = False is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = True is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = ➜ 𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲 :- {file_caption}

➜ 𝗦𝗶𝘇𝗲 :- {file_size}

<b>Join [MBBS NEW 2K Movies](https://t.me/+BBZZe9HKW0I3ZjM1) For More Updates</b>

<b>Powdered By [LinkZz_MBBS](https://t.me/LinkZz_MBBS)</b> environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = ➜ 𝗙𝗶𝗹𝗲 𝗡𝗮𝗺𝗲 :- {file_caption}

➜ 𝗦𝗶𝘇𝗲 :- {file_size}

<b>Join [MBBS NEW 2K Movies](https://t.me/+BBZZe9HKW0I3ZjM1) For More Updates</b>

<b>Powdered By [LinkZz_MBBS](https://t.me/LinkZz_MBBS)</b> environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
