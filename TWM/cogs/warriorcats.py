import random
import discord
import ascyncio
from helpers.sv_config import get_config
from discord.ext import commands
from discord.ext.commands import Cog
from helpers.datafiles import fill_profile
from helpers.placeholders import random_msg

class warrriorcats(Cog)
    """Stuff I added because I'm too addicted."""
    
    @commands.command()
    async def warriorname(self, ctx, mention: str | discord.User = None):
        """Generates your warrior name.
        It's always the same, unless you change it with warriorname set.
        
        - `mention`
        The user to get the warrior name of. Defaults to you. Set to random for a random name. Optional."""
        if mention == None:
            mention = ctx.author.mention

        if isinstance(mention, discord.User):
            random.seed(a=mention.id, version=2)
        elif mention == "random":
            random.seed(a=None, version=2)
        else:
            random.seed(a=mention, version=2)
        name = random_msg("prefix")+random_msg("suffix")
	clan = random_msg("clan")
        await ctx.send(f"Your warrior name is {name} from {clan}.")
        random.seed(a=None, version=2)
        
    
    @warriorname.command(name="set prefix")
    async def warriorname_set_prefix(self, ctx, prefix: str):
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
        else:
            await ctx.send("That's not a valid prefix. Only prefixes from the series are allowed.")
            
    @warriorname.command(name="set suffix")
    async def warriorname_set_suffix(self, ctx, suffix: str):
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
        else:
            await ctx.send("That's not a valid suffix. Only suffixes from the series are allowed.")
            
    @warriorname.command(name="set clan")
    async def warriorname_set_prefix(self, ctx, prefix: str):
        """Sets your clan.
        Legal home changer?!?!?
        
        - `clan`
        The clan you want to set. Can only be from the actual series."""
        profile = fill_profile(ctx.author.id)
        with open("assets/placeholders.yml", "r") as f:
            placeholders = yaml.safe_load(f)
        normal_clans = placeholders["clan"]
        clan = clan.lower().title().replace("clan", "Clan")
        if clan in normal_clans:
            profile["wcclan"] = clan
        else:
            await ctx.send("That's not a valid clan. Only clans from the series are allowed.")
            
    #@commands.command()
    #async def warriorappearance(self, ctx):
        
async def setup(bot):
    await bot.add_cog(Basic(bot))