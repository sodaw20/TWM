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
        
    async def post_random(self,ctx,folder: str, append_path: bool = True) -> None:
        """The LAZIEST function.
        Pass False if folder isn't under assets/random.
        """
        if append_path:
            folder = "assets/random/" + folder
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
            ),
            mention_author=False
        )

    @commands.command(aliases=["Niko"])
    async def niko(self, ctx):
        """Posts a random Niko.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random(ctx,"niko")

    @commands.command(aliases=["Alula"])
    async def alula(self, ctx):
        """Posts a random Alula.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random(ctx,"alula")

    @commands.command(aliases=["Bookbot"])
    async def bookbot(self, ctx):
        """Posts a random Bookbot.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random(ctx,"bookbot")

    @commands.command(aliases=["Calamus"])
    async def calamus(self, ctx):
        """Posts a random Calamus.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random(ctx,"calamus")

    @commands.command(aliases=["Cedric"])
    async def cedric(self, ctx):
        """Posts a random Cedric.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random(ctx,"cedric")
        
    @commands.command(aliases=["Gatekeeper"])
    async def gatekeeper(self, ctx):
        """Posts a random Gatekeeper.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random(ctx,"gatekeeper")

    @commands.command(aliases=["George"])
    async def george(self, ctx):
        """Posts a random George.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random(ctx,"george")

    @commands.command(aliases=["Kelvin"])
    async def kelvin(self, ctx):
        """Posts a random Kelvin.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random(ctx,"kelvin")

    @commands.command(aliases=["Kip"])
    async def kip(self, ctx):
        """Posts a random Kip.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("kip")

    @commands.command(aliases=["Ling"])
    async def ling(self, ctx):
        """Posts a random Ling.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("ling")

    @commands.command(aliases=["Magpie"])
    async def magpie(self, ctx):
        """Posts a random Magpie.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("magpie")

    @commands.command(aliases=["Maize"])
    async def maize(self, ctx):
        """Posts a random Maize.

        There really isn't much else to this.

        No arguments."""

        await self.post_random("maize")

    @commands.command(aliases=["Mason"])
    async def mason(self, ctx):
        """Posts a random Mason.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("mason")

    @commands.command(aliases=["Plight"])
    async def plight(self, ctx):
        """Posts a random Plight.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("plight")

    @commands.command(aliases=["Phrophet", "Prophetbot", "prophetbot"])
    async def prophet(self, ctx):
        """Posts a random Prophet.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("prophet")

    @commands.command(aliases=["Proto", "Prototype", "prototype"])
    async def proto(self, ctx):
        """Posts a random Proto.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("proto")

    @commands.command(aliases=["Rowbot"])
    async def rowbot(self, ctx):
        """Posts a random Rowbot.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("rowbot")

    @commands.command(aliases=["Rue"])
    async def rue(self, ctx):
        """Posts a random Rue.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("rue")
        
    @commands.command(aliases=["Shepard"])
    async def shepard(self, ctx):
        """Posts a random Shepard.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("shepard")

    @commands.command(aliases=["Silver"])
    async def silver(self, ctx):
        """Posts a random Silver.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("silver")

    @commands.command(aliases=["Watcher"])
    async def watcher(self, ctx):
        """Posts a random Watcher.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("watcher")

    @commands.command(
        aliases=[
            "WorldMachine",
            "Worldmachine",
            "en",
            "twm",
            "TWM",
            "Entity",
            "entity",
            "wm",
            "WM",
            "TheWorldMachine",
            "theworldmachine",
        ]
    )
    async def worldmachine(self, ctx):
        """Posts a random World Machine.

        There really isn't much else to this.

        No arguments."""
        
        await self.post_random("wm")

async def setup(bot):
    await bot.add_cog(Random(bot))
