import logging
import discord
from discord.ext import commands

FILE_LOGGING = True
FILE_LOGGING_LEVEL = logging.DEBUG
FILE_LOGGING_FORMATTER = logging.Formatter(
    '%(asctime)s: %(levelname)s: %(name)s => %(message)s')

if FILE_LOGGING:
    logger = logging.getLogger('discord')
    logger.setLevel(FILE_LOGGING_LEVEL)
    handler = logging.FileHandler(
        filename='discord.log', encoding='utf-8', mode='w')
    handler.setFormatter(FILE_LOGGING_FORMATTER)
    logger.addHandler(handler)
else:
    logger = logging.getLogger(__file__)


intents = discord.Intents.default()
intents.members = True

gbot = commands.Bot(command_prefix="!", description="The enlightened one is amongst you.", intents=intents)

@gbot.command()
async def send_dm(ctx, message: str):
    current_guild = ctx.guild
    for member in current_guild.members:
        if member.bot:
            continue
        channel = await member.create_dm()
        await channel.send(message)
        logger.info("Broadcast message successfully sent")
        logger.info(f"Content: {message}")

@gbot.event
async def on_ready():
    logger.info("Bot is running")