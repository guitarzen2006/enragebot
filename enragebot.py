from decouple import config
import os
import discord
import requests
  
BOT_TOKEN = config('TOKEN')
client = discord.Client()


def get_insult():
  response = requests.get("https://evilinsult.com/generate_insult.php")
  return (response.text)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$insult'):
    insult = get_insult()
    await message.channel.send(f"Hey @Adam, {insult}")

client.run(BOT_TOKEN)