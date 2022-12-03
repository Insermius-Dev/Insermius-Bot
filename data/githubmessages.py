import asyncio
import os
import re
import textwrap
import traceback
from pathlib import Path


import aiohttp
import github.GithubException
from github import Github
from naff import (
    Extension,
    Message,
    Embed,
    MaterialColors,
    listen,
    ButtonStyles,
    Button,
    component_callback,
    ComponentContext,
)


class GithubMessages(Extension):
    async def send_snippet(self, message: Message):
        results = snippet_regex.findall(message.content)[0]

        lines = (
            [int(re.sub("[^0-9]", "", line)) for line in results[4].split("-")]
            if len(results) >= 5
            else None
        )
        if not lines:
            return
        user = results[0]
        repo = results[1]
        branch = results[2]
        file = results[3]
        extension = file.split(".")[-1]

        raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{file}"

        async with aiohttp.ClientSession() as session:
            async with session.get(raw_url) as resp:
                if resp.status != 200:
                    return

                file_data = await resp.text()
                if file_data and lines:
                    lines[0] -= 1  # account for 0 based indexing
                    sample = file_data.split("\n")
                    if len(lines) == 2:
                        sample = sample[lines[0] :][: lines[1] - lines[0]]
                        file_data = "\n".join(sample)
                    else:
                        file_data = sample[lines[0]]

                embed = Embed(
                    title=f"{user}/{repo}",
                    description=f"```{extension}\n{textwrap.dedent(file_data)}```",
                )

                await self.reply(message, embeds=embed)

    @listen()
    async def on_message_create(self, event):
        message = event.message
        try:
            if message.author.bot:
                return
            in_data = message.content.lower()

            data = None
            try:

                if "github.com/" in in_data and "#l" in in_data:
                    print("searching for link")
                    return await self.send_snippet(message)

            except github.UnknownObjectException:
                print(f"No git object with id: {data.group().split('#')[-1]}")
        except github.GithubException:
            pass
        except Exception as e:
            print("".join(traceback.format_exception(type(e), e, e.__traceback__)))


def setup(bot):
    GithubMessages(bot)
