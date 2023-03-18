from naff import *
import json


class Tags(Extension):
    @slash_command(name="tag", description="Get, create and print tags.")
    @slash_option(
        name="create_tag",
        description="Create a tag.",
        required=False,
        opt_type=OptionTypes.STRING,
    )
    @slash_option(
        name="tag_list",
        description="Get a list of the already existing tags.",
        required=False,
        opt_type=OptionTypes.BOOLEAN,
    )
    @slash_option(
        name="print_tag",
        description="Print a tag.",
        required=False,
        opt_type=OptionTypes.MENTIONABLE,
    )
    async def tag(self, ctx, create_tag=None, tag_list=None, print_tag=None):
        if create_tag == None and tag_list == None and print_tag == None:
            await ctx.send("Pick an option!", ephmeral=True)
            return
        elif create_tag != None and tag_list != None and print_tag != None:
            await ctx.send("Pick only one option!", ephmeral=True)
            return
        elif create_tag != None and tag_list != None:
            await ctx.send("Pick only one option!", ephmeral=True)
            return
        elif create_tag != None and print_tag != None:
            await ctx.send("Pick only one option!", ephmeral=True)
            return
        elif tag_list != None and print_tag != None:
            await ctx.send("Pick only one option!", ephmeral=True)
            return

        if create_tag != None:
            with open("data/tags.json", "r") as f:
                tags = json.load(f)
            my_modal = Modal(
                title="Create tag",
                components=[
                    ShortText(
                        label="Tag name",
                        custom_id="tag_name",
                        placeholder="Tag name",
                        required=True,
                        max_length=25,
                    ),
                    ParagraphText(
                        label="Tag content",
                        custom_id="tag_content",
                        placeholder="Tag content",
                        required=True,
                        max_length=3500,
                    ),
                ],
            )
            await ctx.send_modal(modal=my_modal)
            modal_ctx: ModalContext = await ctx.bot.wait_for_modal(my_modal)
            if tags.get(modal_ctx.responses["tag_name"]) != None:
                await ctx.send("Tag already exists!", ephmeral=True)
            else:
                tags[modal_ctx.responses["tag_name"]] = modal_ctx.responses["tag_content"]
                with open("data/tags.json", "w") as f:
                    json.dump(tags, f, indent=4)
                await ctx.send(f"Tag '{modal_ctx.responses['tag_name']}' created!")
        elif tag_list != None:
            embed = Embed(
                title="Tag list", description="Here is a list of all the already existing tags:"
            )
            with open("data/tags.json", "r") as f:
                tags = json.load(f)
            for i in range(len(tags)):
                tag = list(tags)[i]
                embed.add_field(name=tag, value=tag[0])

        elif print_tag != None:
            with open("data/tags.json", "r") as f:
                tags = json.load(f)
            if tags.get(print_tag) != None:
                await ctx.send(tags[print_tag])


def setup(bot):
    Tags(bot)
