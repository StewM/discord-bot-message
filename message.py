import os, sys, discord, asyncio, pkgutil
from os.path import join, dirname
from dotenv import load_dotenv

# initialize Discord Client
client = discord.Client()

# load .env file
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# get environment variables
DISCORD_KEY = os.environ.get('DISCORD_KEY')
SERVER = os.environ.get('SERVER')
CHANNEL = os.environ.get('CHANNEL')

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('Sending to:')
    serverobj = client.get_server(SERVER)
    print(serverobj)
    channelobj = serverobj.get_channel(CHANNEL)
    print(channelobj)
    print('Press Ctrl+C twice to quit.')
    print('------')

    while True:
        text = input("What message do you want to send? ")
        await client.send_message(channelobj, text)

client.run(DISCORD_KEY)