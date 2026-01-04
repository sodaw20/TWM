import discord
import os
import asyncio
import random
from discord.ext import commands
from discord.ext.commands import Cog
import html
import json


class Random(Cog):
    """Random OneShot sprites!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def niko(self, ctx):
        """Posts a random Niko.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/niko"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def alula(self, ctx):
        """Posts a random Alula.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/alula"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def bookbot(self, ctx):
        """Posts a random Bookbot.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/bookbot"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def calamus(self, ctx):
        """Posts a random Calamus.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/calamus"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def cedric(self, ctx):
        """Posts a random Cedric.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/cedric"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def gatekeeper(self, ctx):
        """Posts a random Gatekeeper.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/gatekeeper"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def george(self, ctx):
        """Posts a random George.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/george"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def kelvin(self, ctx):
        """Posts a random Kelvin.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/kelvin"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def kip(self, ctx):
        """Posts a random Kip.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/kip"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def ling(self, ctx):
        """Posts a random Ling.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/ling"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def magpie(self, ctx):
        """Posts a random Magpie.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/magpie"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def maize(self, ctx):
        """Posts a random Maize.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/maize"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def mason(self, ctx):
        """Posts a random Mason.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/mason"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def plight(self, ctx):
        """Posts a random Plight.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/plight"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def prophet(self, ctx):
        """Posts a random Prophet.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/prophet"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def proto(self, ctx):
        """Posts a random Proto.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/proto"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def rowbot(self, ctx):
        """Posts a random Rowbot.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/rowbot"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def rue(self, ctx):
        """Posts a random Rue.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/rue"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def shepard(self, ctx):
        """Posts a random Shepard.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/shepard"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def silver(self, ctx):
        """Posts a random Silver.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/silver"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def watcher(self, ctx):
        """Posts a random Watcher.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/watcher"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )

    @commands.command()
    async def worldmachine(self, ctx):
        """Posts a random World Machine.

        There really isn't much else to this.

        No arguments."""
        folder = "assets/random/wm"

        await ctx.reply(
            file=discord.File(
                folder
                + "/"
                + random.choice(
                    [
                        f
                        for f in os.listdir(folder)
                        if os.path.isfile(os.path.join(folder, f))
                    ]
                )
            ),
            mention_author=False,
        )


async def setup(bot):
    await bot.add_cog(Random(bot))
