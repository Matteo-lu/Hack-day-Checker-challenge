import discord
import re
from api.api_script import get_info

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

    if re.match(re.compile("Scrap me", re.I), message.content):
        message_split = message.content.replace("Scrap me ", "").split("/")
        tasks = get_info(message_split[0], message_split[1])
        formated_projects = []
        await message.channel.send("Your current projects are:")
        for project in tasks:
            formated_projects.append("Project name: {}\n\t\t Tasks: {}\n\t\t Checker available: {}".format(project['name'], project['tasks'], project['checker']))
        await message.channel.send("\n".join(formated_projects))

client.run("ODkzNTg3NDQ0OTEyNDkyNTY1.YVdoKA.yZQSW_tIL2kJqD8BmePp8zGpJWk")
