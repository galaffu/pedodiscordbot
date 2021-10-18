import discum
import discord
from discord.ext import commands

client = discord.Client()


bot = discum.Client(token="ODk3MTgxMTE3ODMxMDg2MTAx.YWR7qg.be-BkFr_IMHquLbD8JvjzlFggZ0")

user = client.get_user(785796153437585419)
client.send_message(discord.Object(id='{user}'), 'hello')