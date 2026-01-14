import random
import discord
import yaml
import json
from helpers.sv_config import get_config
from discord.ext import commands
from discord.ext.commands import Cog
from helpers.datafiles import fill_profile, set_userfile
from helpers.placeholders import random_msg

class Warriors(Cog):
    """Stuff I added because I'm too addicted."""

    @commands.group(invoke_without_command=True)
    async def warriorname(self, ctx):
        """Commands to do with your warrior name.

        It's always the same, unless you change it with warriorname set.
        You can view it with warriorname get.
        
        No arguments."""
        return

    @warriorname.group(invoke_without_command=True, name="set")
    async def wcsetname(self, ctx):
        """Commands to do with your warrior name.

        It's always the same, unless you change it with warriorname set.
        You can view it with warriorname get.
        
        No arguments."""
        return

    @warriorname.command(name="get")
    async def wcgetname(self, ctx, mention: str | discord.User = None):
        """Gets your warrior name.

        It's always the same, unless you change it with warriorname set.
        
        - `mention`
        The user to get the warrior name of. Defaults to you. Set to random for a random name. Optional."""
        if mention == None:
            mention = ctx.author.mention
        profile = fill_profile(ctx.author.id)
        if isinstance(mention, discord.User):
            random.seed(a=mention.id, version=2)
        elif mention == "random":
            random.seed(a=None, version=2)
        else:
            random.seed(a=mention, version=2)
        
        prefix = random_msg("prefix") if profile["wcprefix"] == None else profile["wcprefix"]
        suffix = random_msg("suffix") if profile["wcsuffix"] == None else profile["wcsuffix"]
        clan = random_msg("random_clans") if profile["wcclan"] == None else profile["wcclan"]
        await ctx.send(f"Your warrior name is {prefix+suffix} from {clan}.")
        random.seed(a=None, version=2)
        
    
    @wcsetname.command(name="prefix")
    async def wcsetprefix(self, ctx, prefix: str):
        """Sets the prefix for your warrior name.

        Legal name changer?!?!?
        
        - `prefix`
        The prefix you want to set. Can only be from the actual series."""
        profile = fill_profile(ctx.author.id)
        with open("assets/placeholders.yml", "r") as f:
            placeholders = yaml.safe_load(f)
        normal_prefixes = placeholders["prefix"]
        prefix = prefix.lower().capitalize()
        if prefix in normal_prefixes:
            profile["wcprefix"] = prefix
            set_userfile(ctx.author.id, "profile", json.dumps(profile))
            await ctx.send(f"Prefix set to {prefix}.")
        else:
            await ctx.send("That's not a valid prefix. Only prefixes from the series are allowed.")
            
    @wcsetname.command(name="suffix")
    async def wcsetsuffix(self, ctx, suffix: str):
        """Sets the suffix for your warrior name.

        Legal name changer?!?!?
        
        - `suffix`
        The suffix you want to set. Can only be from the actual series."""
        profile = fill_profile(ctx.author.id)
        with open("assets/placeholders.yml", "r") as f:
            placeholders = yaml.safe_load(f)
        normal_suffixes = placeholders["suffix"]
        suffix = suffix.lower()
        if suffix in normal_suffixes:
            profile["wcsuffix"] = suffix
            set_userfile(ctx.author.id, "profile", json.dumps(profile))
            await ctx.send(f"Suffix set to {suffix}.")
        else:
            await ctx.send("That's not a valid suffix. Only suffixes from the series are allowed.")
            
    @wcsetname.command(name="clan")
    async def wcsetclan(self, ctx, clan: str):
        """Sets your clan.

        Legal home changer?!?!?
        
        - `clan`
        The clan you want to set. Can only be from the actual series."""
        profile = fill_profile(ctx.author.id)
        with open("assets/placeholders.yml", "r") as f:
            placeholders = yaml.safe_load(f)
        normal_clans = placeholders["clans"]
        clan = clan.lower().title().replace("clan", "Clan")
        if clan in normal_clans:
            profile["wcclan"] = placeholders["clan_emojis"][clan] + " " + clan
            set_userfile(ctx.author.id, "profile", json.dumps(profile))
            await ctx.send(f"Clan set to {placeholders["clan_emojis"][clan]+ " " + clan}.")
        else:
            await ctx.send("That's not a valid clan. Only clans from the series are allowed.")
            
    #@commands.command()
    #async def warriorappearance(self, ctx):
        
async def setup(bot):
    await bot.add_cog(Warriors(bot))