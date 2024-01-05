import discord
from discord.ext import commands
import datetime
import logging

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) #Creates the bot instance
blacklisted_words = ["fuck", "bitch", "whore", "slut"] 
BOT_TOKEN = "MTEwMTIzMTcyMjM0OTIxNTc4NA.G1DRrL.M1jdssccITir0tcb7JGXa3cTN_7i1-Rv9wfd9k"
#idFile = open("channel.txt", "r") #reads the channel ID from a file so it doesn't have to be hard coded
#CHANNEL_ID = int(idFile.read())
#idFile = close("channel.txt")
#print(CHANNEL_ID)
CHANNEL_ID = 1020870676388790338 #backup for testing

@bot.event
async def on_ready():
    print("Hello! Bot is ready")
    channel = bot.get_channel(CHANNEL_ID) #gets the correct channel from the channel ID


#function for easily sending a DM to a user
async def send_dm(member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

@bot.event
async def on_message(message):
    message_content = message.content
    message_author = message.author 
    for item in blacklisted_words: 
        if item in message_content:
            await message.delete() 
            channel = bot.get_channel(CHANNEL_ID)
            await channel.send(str.format("{} Watch your language", message_author.mention))
            await send_dm(message_author, content="Please refrain from using inappropriate language.")
    print(f'New message -> {message_author} said: {message_content}')


@bot.event
async def on_message_edit(message_before, message): 
    message_content = message.content 
    message_author = message.author 
    for item in blacklisted_words: 
        if item in message_content: 
            await message.delete() 
            channel = bot.get_channel(CHANNEL_ID)
            await channel.send(str.format("{} Watch your language", message_author.mention)) 
            await send_dm(message_author, content="Please refrain from using inappropriate language.") 

    print(f'New message -> {message_author} said: {message_content}')

#ctx, member: discord.Member, duration: int
@bot.command(name="timeout")
async def timeout(ctx, member: discord.Member, duration: int):
    print("balls")
    logging.warning('Watch out!')
    for channel in ctx.guild.channels:
        await channel.set_permissions(member, send_messages=False, speak=False)
    await ctx.send(f"{member.mention} has been timed out for {duration} seconds.")

    
    
bot.run(BOT_TOKEN)
