import discord
import os

import responses

import re
import random

import config

permissions_integer = config.permissions_integer
application_id = config.application_id
public_key = config.public_key
invite_url = config.invite_url
TOKEN = config.TOKEN

async def send_message(message, user_message, is_private):
    try:
        with open('regis.png', 'rb') as f:
            regis = discord.File(f)
        response = responses.get_response(user_message)
        await message.author.send(response, file=regis) if is_private else await message.channel.send(response, file=regis)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content).lower()
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if isRegisMessage(user_message):
            await send_message(message, user_message, is_private=False)
        else:
            pass

    client.run(TOKEN)

def isRegisMessage(message):
    r = re.compile('r.*e.*g.*i.*s')
    if r.match(message):
        if random.randint(1,100) > 75:
            return True
    if 'regis' in message:
        return True
    return False
