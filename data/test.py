import berserk as lichess
from dotenv import load_dotenv
import os
from naff import *
import datetime

load_dotenv()
api_key = os.getenv("LICHESS_API")

session = lichess.TokenSession(api_key)
client = lichess.Client(session=session)

print(client.users.get_public_data("FlopTheMost")["perfs"])
