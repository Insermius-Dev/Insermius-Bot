import urllib, json
from urllib.request import urlopen

player = input("Enter a chess.com username: ")

url = f"https://api.chess.com/pub/player/{player}/stats"

response = urlopen(url)

data = json.loads(response.read())

if data.get("chess_rapid") == None:
    rapid = 0
    rapid_wins = 0
    rapid_losses = 0
    rapid_draws = 0
else:
    rapid = (
        data.get("chess_rapid").get("record").get("win")
        + data.get("chess_rapid").get("record").get("loss")
        + data.get("chess_rapid").get("record").get("draw")
    )
    rapid_draws = data.get("chess_rapid").get("record").get("draw")
    rapid_losses = data.get("chess_rapid").get("record").get("loss")
    rapid_wins = data.get("chess_rapid").get("record").get("win")

if data.get("chess_bullet") == None:
    bullet = 0
    bullet_wins = 0
    bullet_losses = 0
    bullet_draws = 0
else:
    bullet = (
        data.get("chess_bullet").get("record").get("win")
        + data.get("chess_bullet").get("record").get("loss")
        + data.get("chess_bullet").get("record").get("draw")
    )
    bullet_draws = data.get("chess_bullet").get("record").get("draw")
    bullet_losses = data.get("chess_bullet").get("record").get("loss")
    bullet_wins = data.get("chess_bullet").get("record").get("win")

if data.get("chess_blitz") == None:
    blitz = 0
    blitz_wins = 0
    blitz_losses = 0
    blitz_draws = 0
else:
    blitz = (
        data.get("chess_blitz").get("record").get("win")
        + data.get("chess_blitz").get("record").get("loss")
        + data.get("chess_blitz").get("record").get("draw")
    )
    blitz_draws = data.get("chess_blitz").get("record").get("draw")
    blitz_losses = data.get("chess_blitz").get("record").get("loss")
    blitz_wins = data.get("chess_blitz").get("record").get("win")

if data.get("chess_daily") == None:
    daily = 0
    daily_wins = 0
    daily_losses = 0
    daily_draws = 0
else:
    daily = (
        data.get("chess_daily").get("record").get("win")
        + data.get("chess_daily").get("record").get("loss")
        + data.get("chess_daily").get("record").get("draw")
    )
    daily_wins = data.get("chess_daily").get("record").get("win")
    daily_losses = data.get("chess_daily").get("record").get("loss")
    daily_draws = data.get("chess_daily").get("record").get("draw")

total = rapid + bullet + blitz + daily

wins_total = daily_wins + blitz_wins + bullet_wins + rapid_wins
losses_total = daily_losses + blitz_losses + bullet_losses + rapid_losses
draws_total = daily_draws + blitz_draws + bullet_draws + rapid_draws

print(f"{player}'s chess.com stats:")
print(f"games: {total}")
print(f"wins: {wins_total}")
print(f"losses: {losses_total}")
print(f"draws: {draws_total}")
