import discord
import re

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

client.run("TOKEN")
