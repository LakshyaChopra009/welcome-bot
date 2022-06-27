import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("I am Alive")

async def on_member_join(member):
    channel = client.get_channel(985583159586459708)
    em = embed=discord.Embed(title="title", description="description", color=0xff0000)
    embed.set_author(name="name", url="url", icon_url="icon")
    embed.set_thumbnail(url="thumbnail")
    embed.add_field(name="field", value="value", inline=False)
    embed.set_footer(text=f"You are our {len(member.guild.members)}member")
    await channel.send(f"Heya {member.mention}🌙", embed=em)


client.run('client id')
