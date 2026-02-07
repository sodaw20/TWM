import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import Cog
from discord import FFmpegPCMAudio, PCMVolumeTransformer
import pafy
import yt_dlp
import urllib.request
import re
import youtube_dlc
import requests


class Voice(Cog):
    """Broken. DO NOT USE!!!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        """This joins your VC channel.

        There's not much more to it.

        No arguments."""
        if ctx.author.voice is None:
            return await ctx.send("You need to be in a voice channel first.")

        channel = ctx.author.voice.channel

        existing_vc = ctx.guild.voice_client
        if existing_vc is not None:
            if getattr(existing_vc, "channel", None) == channel:
                return await ctx.send(f"I'm already in **{channel}**")
            await existing_vc.move_to(channel)
            return await ctx.send(f"Moved to **{channel}**")

        try:
            await channel.connect(reconnect=False)
        except discord.errors.ConnectionClosed as e:
            code = getattr(e, "code", None)
            return await ctx.send(
                f"Failed to connect to voice (close code {code}). "
                "This is usually a Discord voice/library issue (often fixed by updating your discord library, "
                "trying a different voice region/channel, and ensuring only one bot instance is running)."
            )

        await ctx.send(f"Joined **{channel}**")

    @commands.command()
    async def leave(self, ctx):
        """This leave your VC channel.

        There's not much more to it.

        No arguments."""
        vc = ctx.guild.voice_client
        if vc is None:
            return await ctx.send("I'm not connected to any voice channel.")

        try:
            await vc.disconnect(force=True)
        except TypeError:
            await vc.disconnect()

        await asyncio.sleep(0.75)
        if ctx.guild.voice_client is None:
            await ctx.send("Left the voice channel.")
        else:
            await ctx.send("An error occured trying to leave the channel.")

    @commands.command()
    async def play(self, ctx, *, arg):
        """
        Checks where the command's author is, searches for the music required, joins the same channel as the command's
        author and then plays the audio directly from YouTube.

        - `arg`
        arg can be url to video on YouTube or just as you would search it normally.
        """
        try:
            voice_channel = ctx.author.voice.channel

        # If command's author isn't connected, return.
        except AttributeError as e:
            print(e)
            await ctx.send("Please connect to the voice channel first!")
            return
        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -probesize 200M",
            "options": "-vn",
            }
        ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        }
        # Finds author's session.
        session = ctx.guild.voice_client

        # Searches for the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                requests.get(arg)
            except Exception as e:
                print(e)
                info = ydl.extract_info(f"ytsearch:{arg}", download=False)["entries"][0]
            else:
                info = ydl.sanitize_info(ydl.extract_info(arg, download=False))

        url = info["url"]
        print(url)
        thumb = info["thumbnails"][0]["url"]
        title = info["title"]

        # Finds an available voice client for the bot.
        voice = ctx.guild.voice_client
        if not voice:
            await voice_channel.connect()
            voice = ctx.guild.voice_client

        await ctx.send(thumb)
        await ctx.send(f"Playing {title}")

        source = discord.FFmpegPCMAudio(source=source)
        voice.play(source)


async def setup(bot):
    await bot.add_cog(Voice(bot))
