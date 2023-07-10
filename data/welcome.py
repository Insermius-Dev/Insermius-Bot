import interactions
from interactions import (
    Extension,
    slash_command,
    slash_option,
    Color,
    Embed,
    ActionRow,
    Button,
    ButtonStyle,
    listen,
    OptionType,
)
from datetime import date, datetime

class welcome(Extension):
    @listen()
    async def on_member_add(self, event):  # When a user joins
        print("User joined")
        print(event.guild.id)
        with open("data/nowelcome.txt", "r") as f:  # Get all joined users
            lines = f.readlines()
            int_lines = [eval(i) for i in lines]
            f.close
        joiner = event.member
        if event.guild.id in int_lines:  # Check if user already joined
            pass
        elif not event.guild.id in int_lines:
            if joiner.bot:  # Check if a bot joined
                embed = Embed(
                    description=f"Application '{joiner.display_name}' was added to the server!",
                    color=Color.from_hex("58f728"),
                )

                embed.set_author("Application added", icon_url=joiner.avatar.url)
                await event.guild.system_channel.send(embed=embed)
            else:  # A regular user joined
                embed = Embed(
                    title=f"Welcome {joiner.display_name}!",
                    description=f"Thanks for joining {joiner.guild.name}!",
                    timestamp=datetime.utcnow(),
                    color=Color.from_rgb(88, 109, 245),
                )
                embed.set_thumbnail(url=joiner.avatar.url)

                message = await event.guild.system_channel.send(
                    f"Welcome {joiner.mention}! :wave: ", embed=embed
                )
                await message.add_reaction("👋")


    @listen()
    async def on_member_remove(self, event):  # On member leave
        with open("data/nowelcome.txt", "r") as f:
            lines = f.readlines()
            int_lines = [eval(i) for i in lines]
            f.close()
        leaver = event.member
        if leaver == self.bot.user:
            pass
        elif event.guild.id in int_lines:
            pass
        elif int(event.guild.id) == 1090004044111696075:
            pass
        elif not event.guild.id in int_lines:
            if leaver.bot:
                embed = Embed(
                    description=f"Application '{leaver.display_name}' was removed from the server!",
                    color=Color.from_hex("f73528"),
                )

                embed.set_author(f"Application removed", icon_url=leaver.avatar.url)
                await event.guild.system_channel.send(embed=embed)
            else:
                embed = Embed(
                    title=f"{leaver.display_name} left.",
                    description=f"Sorry to see you go {leaver.display_name}!",
                    timestamp=datetime.utcnow(),
                    color=Color.from_rgb(255, 13, 13),
                )

                await event.guild.system_channel.send(embed=embed)
    
    # TODO: Fix the invite creation
    @listen()
    async def on_guild_join(self, event):
        if self.bot.is_ready:
            print("New guild joined")
            dm = self.bot.owner
            invites = []
            best_invite = None
            for channel in event.guild.channels:
                channel_invites = await channel.fetch_invites()
                for invite in channel_invites:
                    invites.append(invite)
            if invites == []:
                print("No invites found. Generating invite...")
                for channel in event.guild.channels:
                    if channel.permissions_for(event.guild.me).create_instant_invite:
                        best_invite = await channel.create_invite() 
                        return
                if invites == []:
                    print("No invite perms")
                    best_invite = ""
            
            if invites != []:
                # calculate the best invite and create an invite if the best invite is bad
                for invite in invites:
                    if invite.max_uses == 0 or invite.max_uses > 10:
                        if invite.max_age == 0 or invite.max_age > 604800:
                            if invite.temporary == False:
                                best_invite = invite
                                break
                if best_invite == None:
                    print("No good invite found. Creating invite...")
                    for channel in event.guild.channels:
                        if channel.permissions_for(event.guild.me).create_instant_invite:
                            best_invite = await channel.create_invite() 
                            return
                    if invites == []:
                        print("No invite perms")
                        best_invite = ""
                
            embed = Embed(
                title=event.guild.name,
                description=event.guild.description,
                timestamp=datetime.utcnow(),
                color=Color.from_hex("32a852"),
                thumbnail=event.guild.icon.url,
            )
            embed.add_field(name="Member count", value=len(event.guild.members))
            embed.add_field(name="Created", value=event.guild.created_at)
            embed.add_field(name="Boost level", value="Level {0}".format(event.guild.premium_tier))
            await dm.send(best_invite.link, embed=embed)
            # with open("data/nowelcome.txt", "w") as f:
            #     lines = f.readlines()
            #     lines.append(event.guild.id)
            #     f.write("\n".join(lines))

    @listen()
    async def on_guild_left(self, event):
        if self.bot.is_ready:
            print("Guild left")
            dm = self.bot.owner
            embed = Embed(
                title="Removed from " + event.guild.name,
                description="",
                timestamp=datetime.utcnow(),
                color=Color.from_hex("b50a07"),
                thumbnail=event.guild.icon.url,
            )
            # with open("data/nowelcome.txt", "w") as f:
            #     lines = f.readlines()
            #     int_lines = [eval(i) for i in lines]
            #     if event.guild.id in int_lines:
            #         int_lines.remove(event.guild.id)
            #         f.write("\n".join(int_lines))
            await dm.send(embed=embed)

def setup(bot):
    welcome(bot)