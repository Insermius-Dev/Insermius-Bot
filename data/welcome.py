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
    Permissions,
)
from datetime import datetime
from const import DELETE_BTN
import asyncio

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
        await asyncio.sleep(3)  # Leave some time for the audit log to be updated
        # audit_logs_bans = await event.guild.fetch_audit_log(
        #     action_type=interactions.AuditLogEventType.MEMBER_BAN_ADD,
        #     after=datetime.now() - timedelta(seconds=4),
        # )
        # audit_logs_kicks = await event.guild.fetch_audit_log(
        #     action_type=interactions.AuditLogEventType.MEMBER_KICK,
        #     after=datetime.now() - timedelta(seconds=4),
        # )

        # audit_log_entry_ban = None
        # audit_log_entry_kick = None

        # if audit_logs_bans.entries is not []:
        #     for entry in audit_logs_bans.entries:
        #         if entry.target.id == event.member.id:
        #             audit_log_entry_ban = entry
        #             break
        # else:
        #     audit_log_entry_ban = None

        # if audit_logs_kicks.entries is not []:
        #     for entry in audit_logs_kicks.entries:
        #         if entry.target.id == event.member.id:
        #             audit_log_entry_kick = entry
        #             break
        # else:
        #     audit_log_entry_kick = None

        # audit_log_ban = await event.guild.fetch_audit_log(
        #     action_type=interactions.AuditLogEventType.MEMBER_BAN_ADD, limit=1
        # )
        # print(audit_log_ban.entries)
        # if audit_log_ban.entries[0].target.id != event.member.id:
        #     audit_log_entry_ban = None
        # elif audit_log_ban.entries[0].date < datetime.now() - timedelta(seconds=4):
        #     audit_log_entry_ban = None

        # audit_log_kick = await event.guild.fetch_audit_log(
        #     action_type=interactions.AuditLogEventType.MEMBER_KICK, limit=None
        # )
        # print(audit_log_kick.entries)
        # if audit_log_kick.entries[0].target.id != event.member.id:
        #     audit_log_entry_kick = None
        # elif audit_log_kick.entries[0].date < datetime.now() - timedelta(seconds=4):
        #     audit_log_entry_kick = None

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
            # elif audit_log_entry_ban is not None:
            #     embed = Embed(
            #         title=f"{leaver.display_name} got banned.",
            #         description=f"{leaver.display_name} was banned from the server by {audit_log_entry_ban.user.display_name}.",
            #         timestamp=datetime.utcnow(),
            #         color=Color.from_rgb(255, 13, 13),
            #     )

            #     await event.guild.system_channel.send(embed=embed)
            # elif audit_log_entry_kick is not None:
            #     if audit_log_entry_kick.target.id == leaver.id:
            #         pass
            #     else:
            #         embed = Embed(
            #             title=f"{leaver.display_name} got kicked.",
            #             description=f"{leaver.display_name} was kicked from the server by {audit_log_entry_kick.user.display_name}.",
            #             timestamp=datetime.utcnow(),
            #             color=Color.from_rgb(255, 13, 13),
            #         )

            #         await event.guild.system_channel.send(embed=embed)
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
            print("Bot ready")
            dm = self.bot.owner
            invites = []
            best_invite = None
            invites = await event.guild.fetch_invites()
            if invites == []:
                print("No invites found. Generating invite...")
                for channel in event.guild.channels:
                    if event.guild.me.has_permission(Permissions.CREATE_INSTANT_INVITE):
                        best_invite = await channel.create_invite(max_age=0)
                        break
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
                        if event.guild.me.has_permission(Permissions.CREATE_INSTANT_INVITE):
                            best_invite = await channel.create_invite(max_age=0)
                            break
                    if invites == []:
                        print("No invite perms")
                        best_invite = ""

            print(best_invite.link)
            await dm.send(best_invite.link)
            embed = Embed(
                title=event.guild.name,
                description=event.guild.description,
                timestamp=datetime.utcnow(),
                color=Color.from_hex("5e50d4"),
                thumbnail=event.guild.icon.url,
            )
            embed.add_field(name="Member count", value=len(event.guild.members))
            embed.add_field(name="Created", value=event.guild.created_at)
            embed.add_field(name="Boost level", value="Level {0}".format(event.guild.premium_tier))
            await dm.send(best_invite.link, embed=embed)

            embed = Embed(
                title="Thanks for adding me to your wonderful server!",
                description="""
I use slash commands. Use /info for some basic info!

If you have any suggestions or issues please report them in my [support server](https://discord.gg/TReMEyBQsh)!
Also check out [my beta website](https://larss-bot.onrender.com)! 

‼ Important note: This bot is still under constant development and may have bugs, issues and other misshappens like random downtime and others. ‼""",
                timestamp=datetime.utcnow(),
                color=Color.from_hex("32a852"),
            )
            embed.set_footer(text="Enjoy!", icon_url=self.bot.owner.avatar.url)
            await event.guild.system_channel.send(embed=embed, components=[DELETE_BTN])
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
                description=str(event.guild.id),
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
