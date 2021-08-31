from typing import Literal

import discord
import requests
import aiohttp
import io
from redbot.core import commands
from redbot.core.bot import Red
from redbot.core.config import Config

RequestType = Literal["discord_deleted_user", "owner", "user", "user_strict"]


class Cat(commands.Cog):
    """
    cat
    """

    def __init__(self, bot: Red) -> None:
        self.bot = bot
        self.cat_api = "https://api.thecatapi.com/v1/images/search"

    @commands.command()
    async def cat(self, ctx):
        """Get random cat"""
        response = requests.get(self.cat_api,params={'x-api-key':'a2db441d-eb55-418f-a4a2-2d45db833c6d'})
        url = response.json()[0].get('url')
        await ctx.send(url)

    def cog_unload(self):
        self.bot.loop.create_task(self.session.close())
