from dotenv import load_dotenv
import os
import interactions
from interactions import *
import re
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from PIL import Image
import requests
from io import BytesIO
from collections import defaultdict
from datetime import date, datetime

load_dotenv()

delete_btn = Button(style=ButtonStyle.RED, custom_id="delete", emoji="🗑️")

scope = None
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
# redirect_url = os.getenv("SPOTIFY_REDIRECT_URL")
redirect_url = "http://localhost:8888/callback"

sp = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
)
sp.trace = False


def get_sp_info(URI):
    if "playlist" in URI:
        playlist_URI = URI.split("/")[-1].split("?")[0]
        try:
            sp.playlist(playlist_URI)["name"]
        except:
            return 404

        contents = ""
        for track in sp.playlist_tracks(playlist_URI)["items"]:
            contents += "> " + track["track"]["name"] + "\n"
            if (
                track["track"]["name"]
                == sp.playlist_tracks(playlist_URI)["items"][19]["track"]["name"]
            ):
                contents += "> ..."
                break

        response = requests.get(sp.playlist(playlist_URI)["images"][0]["url"])
        img = Image.open(BytesIO(response.content))

        by_color = defaultdict(int)
        for pixel in img.getdata():
            by_color[pixel] += 1

        # get the most common color
        clr = max(by_color.items(), key=lambda x: x[1])[0]

        embed = Embed(
            title=sp.playlist(playlist_URI)["name"],
            description=f'Made by {sp.playlist(playlist_URI)["owner"]["display_name"]}.',
            color=Color.from_rgb(clr[0], clr[1], clr[2]),
        )
        embed.add_field(
            name="Contents",
            value=contents,
        )
        embed.set_thumbnail(url=sp.playlist(playlist_URI)["images"][0]["url"])
        return embed

    elif "album" in URI:
        album_URI = URI.split("/")[-1].split("?")[0]
        try:
            sp.album(album_URI)["name"]
        except:
            return 404

        contents = ""
        for track in sp.album_tracks(album_URI)["items"]:
            contents += "> " + track["name"] + "\n"
            if len(sp.album_tracks(album_URI)["items"]) >= 20:
                if track["name"] == sp.album_tracks(album_URI)["items"][19]["name"]:
                    contents += "> ..."
                    break

        authors = ""
        for author in sp.album(album_URI)["artists"]:
            if author == sp.album(album_URI)["artists"][-1]:
                authors += author["name"]
            else:
                authors += author["name"] + ", "

        response = requests.get(sp.album(album_URI)["images"][0]["url"])
        img = Image.open(BytesIO(response.content))

        by_color = defaultdict(int)
        for pixel in img.getdata():
            by_color[pixel] += 1

        # get the most common color
        clr = max(by_color.items(), key=lambda x: x[1])[0]

        embed = Embed(
            title=sp.album(album_URI)["name"],
            description=f"Album by {authors}.",
            color=Color.from_rgb(clr[0], clr[1], clr[2]),
        )
        embed.set_thumbnail(url=sp.album(album_URI)["images"][0]["url"])
        embed.add_field(
            name="Contents",
            value=contents,
        )
        return embed

    elif "track" in URI:
        song_URI = URI.split("/")[-1].split("?")[0]
        try:
            sp.track(song_URI)["name"]
        except:
            return 404

        description = f'{sp.track(song_URI)["name"]} by '
        for artist in sp.track(song_URI)["artists"]:
            # if artist last in list dont add coma
            if artist == sp.track(song_URI)["artists"][-1]:
                description += f'{artist["name"]}.'
            else:
                description += f'{artist["name"]}, '

        response = requests.get(sp.track(song_URI)["album"]["images"][0]["url"])
        img = Image.open(BytesIO(response.content))

        by_color = defaultdict(int)
        for pixel in img.getdata():
            by_color[pixel] += 1

        # get the most common color
        clr = max(by_color.items(), key=lambda x: x[1])[0]

        embed = Embed(
            title=sp.track(song_URI)["name"],
            description=description,
            color=Color.from_rgb(clr[0], clr[1], clr[2]),
        )
        embed.set_thumbnail(url=sp.track(song_URI)["album"]["images"][0]["url"])
        return embed

    elif "artist" in URI:
        artist_URI = URI.split("/")[-1].split("?")[0]
        try:
            sp.artist(artist_URI)["name"]
        except:
            return 404

        top5 = ""
        for i in range(len(sp.artist_top_tracks(artist_URI)["tracks"])):
            top5 += "> " + sp.artist_top_tracks(artist_URI)["tracks"][i]["name"] + "\n"
            if i == 4:
                break

        # split the number to make it more readable
        monthly_listeners = str(sp.artist(artist_URI)["followers"]["total"])
        monthly_listeners = monthly_listeners[::-1]
        monthly_listeners = ",".join(
            [monthly_listeners[i : i + 3] for i in range(0, len(monthly_listeners), 3)]
        )
        monthly_listeners = monthly_listeners[::-1]

        response = requests.get(sp.artist(artist_URI)["images"][0]["url"])
        img = Image.open(BytesIO(response.content))

        by_color = defaultdict(int)
        for pixel in img.getdata():
            by_color[pixel] += 1

        # get the most common color
        clr = max(by_color.items(), key=lambda x: x[1])[0]

        embed = Embed(
            title=sp.artist(artist_URI)["name"],
            description=f"{monthly_listeners} monthly listeners.",
            color=Color.from_rgb(clr[0], clr[1], clr[2]),
        )
        embed.set_thumbnail(url=sp.artist(artist_URI)["images"][0]["url"])
        embed.add_field(
            name="Top 5 songs",
            value=top5,
        )
        return embed

    # check if its a user
    elif "user" in URI:
        user_URI = URI.split("/")[-1].split("?")[0]
        try:
            sp.user(user_URI)["display_name"]
        except:
            return 404

        playlists = 0
        for playlist in sp.user_playlists(user_URI)["items"]:
            if playlist["owner"]["id"] == user_URI:
                playlists += 1

        response = requests.get(sp.user(user_URI)["images"][0]["url"])
        img = Image.open(BytesIO(response.content))

        by_color = defaultdict(int)
        for pixel in img.getdata():
            by_color[pixel] += 1

        # get the most common color
        clr = max(by_color.items(), key=lambda x: x[1])[0]

        embed = Embed(
            title=sp.user(user_URI)["display_name"],
            description=f'{sp.user(user_URI)["followers"]["total"]} followers',
            color=Color.from_rgb(clr[0], clr[1], clr[2]),
        )
        embed.set_thumbnail(url=sp.user(user_URI)["images"][0]["url"])
        embed.add_field(
            name="Public playlists",
            value=f"{playlists} public playlists",
        )
        return embed


class spotify(Extension):
    @listen()
    async def on_message_create(self, ctx):
        if ctx.message.author == self.bot.user:
            return

        regex = r"https:\/\/open\.spotify\.com\/(track|album|playlist|artist|user)\/[a-zA-Z0-9]+(\?si=[a-zA-Z0-9]+)?"

        matches = re.finditer(regex, ctx.message.content, re.MULTILINE)

        embeds = []

        # return all matches
        for matchNum, match in enumerate(matches, start=1):
            # initiate a typing state on the channel
            await ctx.message.channel.trigger_typing()
            callback = get_sp_info(match.group())
            if callback == 404:
                embed = Embed(
                    title="Error",
                    description="Invalid URL",
                    color=0x808080,
                )
                embeds.append(embed)
            else:
                embeds.append(callback)

        if embeds != []:
            await ctx.message.reply(embeds=embeds, components=[delete_btn])

    @slash_command(
        name="spotify",
        description="Share what you're listening to!",
    )
    async def spotify(self, ctx):
        listener = ctx.author

        # Get the first activity that contains "Spotify". Return None, if none present.
        spotify_activity = next((x for x in listener.activities if x.name == "Spotify"), None)

        if spotify_activity is not None:
            cover = f"https://i.scdn.co/image/{spotify_activity.assets.large_image.split(':')[1]}"
            response = requests.get(cover)

            img = Image.open(BytesIO(response.content))

            by_color = defaultdict(int)
            for pixel in img.getdata():
                by_color[pixel] += 1
            # get the most common color
            clr = max(by_color.items(), key=lambda x: x[1])[0]
            embed = Embed(
                title=f"{listener.display_name}'s Spotify",
                description="Listening to {}".format(spotify_activity.details),
                color=Color.from_rgb(clr[0], clr[1], clr[2]),
                thumbnail=cover,
            )
            embed.add_field(name="Artist", value=spotify_activity.state)
            embed.add_field(name="Album", value=spotify_activity.assets.large_text)
        else:
            embed = Embed(
                title=f"{listener.display_name}'s Spotify",
                description="Currently not listening to anything",
                color=0x808080,
                timestamp=datetime.utcnow(),
            )
        embed.set_footer(text="Requested by " + str(ctx.author), icon_url=ctx.author.avatar.url)
        message = await ctx.send(embeds=embed, components=[delete_btn])
        # await message.add_reaction(spotify_emoji)


def setup(bot):
    spotify(bot)
