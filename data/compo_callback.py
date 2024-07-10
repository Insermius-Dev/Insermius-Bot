from interactions import *
from datetime import *
from const import DELETE_BTN, EPIC_CONTRIBUTING_PPL, LIL_HELPERS, NAMEDAYS_EXT


class callback(Extension) :

    @listen()
    async def on_component(self, ctx: ComponentContext):
        event = ctx.ctx
        match event.custom_id:
            case "contributors":
                message_components = event.message.components
                message_components[0].components[0].disabled = True
                await event.message.edit(components=message_components)

                embed = Embed(
                    title="⭐ Contributors",
                    description=f"Awesome people who have helped to make Larss_Bot what it is today!",
                    timestamp=datetime.now(),
                    color=Color.from_hex("5e50d4"),
                    footer=EmbedFooter(text=f"Requested by {event.author.display_name}", icon_url=event.author.avatar.url)
                )
                value = ""
                for contributor in EPIC_CONTRIBUTING_PPL:
                    value += f"> <@{contributor}> \n"

                embed.add_field(
                    name="Contributors",
                    value=value,
                )

                value = ""
                for lilhelper in LIL_HELPERS:
                    value += f"> <@{lilhelper}> \n"

                embed.add_field(
                    name="Little helpers",
                    value=value,
                )
                await event.send(embed=embed, components=[DELETE_BTN])

            case "guildsinvites":
                message_components = event.message.components
                message_components[0].components[1].disabled = True
                await event.message.edit(components=message_components)

                embed = Embed(
                    title="Partner servers",
                    description=f"Press any of the buttons below to get invited to one of the partnered servers",
                    timestamp=datetime.now(),
                    color=Color.from_hex("5e50d4"),
                    footer=EmbedFooter(text=f"Requested by {event.author.display_name}", icon_url=event.author.avatar.url)
                )

                btn1 = Button(
                    style=ButtonStyle.URL,
                    label="Dev lab",
                    emoji="🧪",
                    url="https://discord.gg/TReMEyBQsh",
                )
                btn2 = Button(
                    style=ButtonStyle.URL,
                    label="Big-Floppa software solutions",
                    emoji="🐱",
                    url="https://discord.gg/MDVcb8wdUd",
                )
                btn3 = Button(
                    style=ButtonStyle.URL,
                    label="Tyler army",
                    emoji="🐸",
                    url="https://discord.gg/w78rcjW8ck",
                )
                components: list[ActionRow] = spread_to_rows(btn1, btn2, btn3)
                components.append(ActionRow(DELETE_BTN))

                await event.send(embed=embed, components=components)
            case "extendedlistshow":
                today = date.today().strftime("%m-%d")
                embed = Embed(
                    title="Visi šodienas vārdi",
                    description="> " + "\n> ".join(NAMEDAYS_EXT[today]),
                    color=Color.from_rgb(255, 13, 13),
                )

                message_components = event.message.components
                message_components[0].components[0].disabled = True
                await event.message.edit(components=message_components)

                await event.send(embed=embed, components=[DELETE_BTN])

            case "delete":
                if event.author.id == 494795032717426688:
                    await event.send("FUCK YOU!! YOU CANT DO THIS!!", ephemeral=True)
                else:
                    try:
                        if (
                            event.message.interaction._user_id == event.author.id
                            or event.author.has_permission(Permissions.MANAGE_MESSAGES)
                        ):
                            await event.message.delete()
                        else:
                            await event.send("Not your interaction.", ephemeral=True)
                    except:
                        if event.author.has_permission(Permissions.MANAGE_MESSAGES):
                            await event.message.delete()
                        else:
                            await event.send("Not your interaction.", ephemeral=True)


def setup(bot):
    callback(bot)