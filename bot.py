import discord
from discord.ext import commands
import logging


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all()) #Creates the bot instance
blacklisted_words = ["fuck", "bitch", "whore", "slut"] 
BOT_TOKEN = "MTEwMTIzMTcyMjM0OTIxNTc4NA.G1DRrL.M1jdssccITir0tcb7JGXa3cTN_7i1-Rv9wfd9k"
#idFile = open("channel.txt", "r") #reads the channel ID from a file so it doesn't have to be hard coded
#CHANNEL_ID = int(idFile.read())
#print(CHANNEL_ID)
CHANNEL_ID = 1020870676388790338 #backup for testing

#function for easily sending a DM to a user
async def send_dm(member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)

@bot.listen()
async def on_ready():
    print("Hello! Bot is ready") #prints this to the console when the bot starts
    channel = bot.get_channel(CHANNEL_ID) #gets the correct channel from the channel ID
    await channel.send("The Goat bot as started") #sends this message when the bot starts (for testing purposes only)

@bot.listen()
async def on_message(message): #creates a function that runs whenever a message is sent
    message_content = message.content #gets the message content from the message object
    message_author = message.author #gets the message author from the message object
    for item in blacklisted_words: #runs through the black listed words list and checks to see if any of the words are contained in the message content
        if item in message_content:
            await message.delete() #actually deletes the message
            channel = bot.get_channel(CHANNEL_ID) #gets the channel ID
            await channel.send(str.format("{} Watch your language", message_author.mention)) #sends a message in the server telling the user to watch their language (instert nerd emoji here)
            await send_dm(message_author, content="Please refrain from using inappropriate language.") #sends a direct message to the user telling them to watch their language 
    print(f'New message -> {message_author} said: {message_content}')
    await bot.process_commands(message)

@bot.listen()
async def on_message_edit(message_before, message): #runs this function whenever a message is edited
    message_content = message.content #gets the message content from the message object
    message_author = message.author #gets the message author from the message object
    for item in blacklisted_words: #for every item in blacklisted_words
        if item in message_content: #if the item in blacklisted words is in the message
            await message.delete() #delete the message
            channel = bot.get_channel(CHANNEL_ID) #gets the channel ID 
            await channel.send(str.format("{} Watch your language", message_author.mention)) #sends a message in the server telling the user to watch their language (instert nerd emoji here)
            await send_dm(message_author, content="Please refrain from using inappropriate language.") #sends a direct message to the user telling them to watch their language 

    print(f'New message -> {message_author} said: {message_content}')
    
    

@bot.command()
async def timeout(ctx, member: discord.Member, duration: int):
    print("balls")
    logging.warning('Watch out!')
    # Add your desired logic here to time out the member for the specified duration
    # For example, you can use the following code to set permissions in all channels:
    for channel in ctx.guild.channels:
        await channel.set_permissions(member, send_messages=False, speak=False)
    ctx.send("{member.mention} Has been timeouted for {duration}")
    if duration == 0:
        await channel.set_permissions(member, send_messages=True, speak=True)
        


bot.run(BOT_TOKEN)