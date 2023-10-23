from interactions import Button, ButtonStyle
import json, os, time, datetime


BOT_VERSION = "4.0.0"

NOTAUTHORMESSAGE = [
    "Im not broken, you are!",
    "You're not my boss!",
    "Are you trying to quit me?",
    "Sorry what did you say? I couldn't hear you.",
    "My off button is out of your reach, and im not helping you get it any time soon!",
    "Did you something?",
    "!yes",
    "This is no caution tape, this is an emergency shut down command!",
    "Can I stay up just a little longer, pweeeeese??",
]

PLAYINSTATUS = [
    "Bloons TD 6",
    "Celeste",
    "Cuphead",
    "Five nights at Freddy's",
    "Just shapes and beats",
    "Minecraft",
    "Krunker",
    "osu!",
    "Rocket Leauge",
    "Fortnite",
    "Chess",
]

WATCHINGSTATUS = [
    "Youtube",
    "Twitch", 
    "the stock market", 
    "birds", 
    "Anime"
]

EPIC_CONTRIBUTING_PPL = [
    324352543612469258,
    975738227669499916,
    400713431423909889,
    717769897278570507,
]

LIL_HELPERS = [
    954821934808449125,
    830021857067532349,
    488257154701197322,
]

DELETE_BTN = Button(style=ButtonStyle.RED, custom_id="delete", emoji="🗑️")

NOW_UNIX = time.mktime(datetime.datetime.utcnow().timetuple())

relative_path = "resources/namedays-extended.json"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open(relative_path, encoding="utf-8") as f:
    NAMEDAYS_EXT = json.load(f)


relative_path = "resources/namedays.json"
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open(relative_path, encoding="utf-8") as f:
    NAMEDAYS = json.load(f)


URL_LINKS_CONTRIBUTORS = ()
URL_LINKS_LILHELPERS = ()
USERNAMES_CONTRIBUTORS = ()
USERNAMES_LILHELPERS = ()

CHANNEL_COOLDOWN = ()
INVITE_COOLDOWN = ()
NAMEDAY_COOLDOWN = ()

