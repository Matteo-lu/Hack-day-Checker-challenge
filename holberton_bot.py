import discord
import re
from intranet_hbn_scraper import intranet_hbn_scraper

client = discord.Client()

@client.event
async def on_ready():
    print("Betto is logged in as {0.user}".format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    if re.match(re.compile("repeat", re.I), message.content):
        await message.channel.send("You just said: {}".format(message.content.replace('repeat', '')))

    if re.match(re.compile("scrap me", re.I), message.content):
        message_split = message.content.replace("scrap me ", "").split("/")
        intranet_hbn_scraper(message_split[0], message_split[1])

client.run("TOKEN")
