from os import getenv
from pathlib import Path
from urllib.parse import urlparse


def extract_domain(var_name, output):
    """
    Extracts just the domain name from an URL and adds it to a list
    """
    var = getenv(var_name)

    if var:
        p = urlparse(var)
        output.append(p.hostname)


def make_whitelist():
    """
    Generates the list of whitelisted domains for webviews. This is especially
    useful when you create your Facebook Messenger configuration.

    Don't hesitate to change this function to add more domains if you need it.
    """
    out = []
    extract_domain("BERNARD_BASE_URL", out)
    return out


def i18n_root(lang) -> Path:
    """
    Computes the root to a given lang's root directory
    """
    return Path(__file__).parent / "../../i18n" / lang


# --- Starting points ---

# This module contains the transitions and is loaded to generate the FSM.
TRANSITIONS_MODULE = "telegram_bot.transitions"

# The default state is used whenever something goes wrong which prevents a
# state to be chosen. In this case, it will ball back to the default state
# in order to produce an error message. This default state must also be the
# common ancestor of all your states in order for them to inherit the default
# error messages.
DEFAULT_STATE = "telegram_bot.baseStates.TelegramBotState"


# --- Platforms ---

# That's the configuration tokens for all the platforms you want to manage.
PLATFORMS = [
        {
            "class": "bernard.platforms.telegram.platform.Telegram",
            "settings": {
                "token": "7497025148:AAF57AVkaaT3AtTihtXmGeDjr6-Gc6QPfhg",
            },
        }
    ]


# Public base URL, used to generate links to the bot itself.
BERNARD_BASE_URL = getenv("BERNARD_BASE_URL")

# Secret key that serves in particular to sign content sent to the webview, but
# also in other places where signed content is required (aka when something
# goes outside and back again).
WEBVIEW_SECRET_KEY = getenv("WEBVIEW_SECRET_KEY")


# --- Network configuration ---

socket_path = getenv("SOCKET_PATH")

# That's a way to configure the network binding. If you define the SOCKET_PATH
# environment variable, then it will bind to the specified path as a UNIX
# socket. Otherwise it will look at BIND_PORT to know which TCP port to bind to
# and will fall back to 8666.
if socket_path:
    SERVER_BIND = {
        "path": socket_path,
    }
else:
    SERVER_BIND = {
        "host": "127.0.0.1",
        "port": int(getenv("BIND_PORT", "8666")),
    }


# --- Natural language understanding/generation ---

# List of intents loaders, typically CSV files with intents.
I18N_INTENTS_LOADERS = [
    {
        "loader": "bernard.i18n.loaders.CsvIntentsLoader",
        "params": {
            "file_path": i18n_root("en") / "intents.csv",
            "locale": "en",
        },
    },
]

# List of translation loaders, typically CSV files with translations.
I18N_TRANSLATION_LOADERS = [
    {
        "loader": "bernard.i18n.loaders.CsvTranslationLoader",
        "params": {
            "file_path": i18n_root("es") / "responses.csv",
            "locale": "es",
        },
    },
]



# --- Middlewares ---

# All your middlewares. The default ones are here to slow down the sending of
# messages and make it look more natural.
MIDDLEWARES = [
    "bernard.middleware.AutoSleep",
    "bernard.middleware.AutoType",
]

# Sleeping offset before any message
USERS_READING_BUBBLE_START = 0.0

# How many words per minute can your users read? This will compute the delay
# for each message automatically.
USERS_READING_SPEED = 400

# This is the chat id for fix sen photo

URL = "https://api.telegram.org/bot7497025148:AAF57AVkaaT3AtTihtXmGeDjr6-Gc6QPfhg/"

