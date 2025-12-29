import discord
from discord.ext import commands, tasks
from discord.ext.commands import Cog
import json
import re
import datetime
import random
import html
import os
from helpers.checks import ismod
from helpers.checks import ismanager
from helpers.sv_config import get_config

class Pfp(Cog):
    """
    Dynamic pfp system.
    """

    def __init__(self, bot):
        self.bot = bot
        self.pfptimer.start()
        self.nocfgmsg = "PFP failed to switch!!"
        self.images = "assets/random/wm"

    def cog_unload(self):
        self.pfptimer.cancel()


    @commands.check(ismanager)
    @commands.command()
    async def rerollpfp(self, ctx):
        """This forcibly rerolls the PFP.

        No arguments."""
        new_avatar=open(
            self.images + "/" + random.choice(
                [
                    f
                    for f in os.listdir(self.images)
                    if os.path.isfile(os.path.join(self.images, f))
                ]
            ),       
            "rb"
        )
        await self.bot.user.edit(avatar=new_avatar.read())
        await ctx.send(content="PFP reloaded!")

    @tasks.loop(time=[datetime.time(hour=x) for x in range(0, 24)])
    async def pfptimer(self):
        await self.bot.wait_until_ready()
        if int(datetime.datetime.now().strftime("%H%M")) == 0000:
            new_avatar=open(
                self.images + "/" + random.choice(
                    [
                        f
                        for f in os.listdir(self.images)
                        if os.path.isfile(os.path.join(self.images, f))
                    ]
                ),       
                "rb"
            )
            await self.bot.user.edit(avatar=new_avatar.read())

async def setup(bot):
    await bot.add_cog(Pfp(bot))