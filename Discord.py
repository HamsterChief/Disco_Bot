import discord
from discord.ext import commands
import random
import asyncio

# Your bot's token
# TOKEN = 'MTMxODU3NDY4MjIzNjI1NjI1Ng.GCRI3W.SDnWOVuhYTo2G4tehTJHr3JRNHd3-kbt5yzggI'

# Enable intents
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content

# Bot prefix and setup
bot = commands.Bot(command_prefix="!", intents=intents)

# Event to confirm bot is ready


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")


@bot.event
async def on_message(message):
    print(f"Received message: {message.content}")
    await bot.process_commands(message)


# @bot.event
# async def on_voice_state_update(member, before, after):
#     # Check if a user has joined a voice channel
#     if before.channel is None and after.channel is not None:
#         voice_channel = after.channel

#         # Wait for a random amount of time (e.g., 30 to 90 seconds)
#         wait_time = random.randint(2, 5)
#         await asyncio.sleep(wait_time)

#         # Recheck if the member is still in the same voice channel
#         if member.voice and member.voice.channel == voice_channel:
#             try:
#                 # Join the voice channel and play a sound
#                 vc = await voice_channel.connect()
#                 vc.play(discord.FFmpegPCMAudio("quack.mp3"))

#                 # Wait until the sound is finished playing
#                 while vc.is_playing():
#                     await asyncio.sleep(1)

#                 # Disconnect after playing the sound
#                 await vc.disconnect()
#             except Exception as e:
#                 print(f"Error playing sound: {e}")


@bot.command()
async def hello(ctx):
    # Sends a message to the channel where the command is called
    await ctx.send("You're a man with a fork in a world of soup")

# Run the bot
bot.run(TOKEN)
