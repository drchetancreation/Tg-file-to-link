from pyrogram import filters
from WebStreamer.bot import StreamBot
from pyrogram.types import Message

@StreamBot.on_message(filters.command('help'))
async def help(_, m: Message):
    await m.reply("If didn't work, Give a click https://gotalink.herokuapp.com/")

@StreamBot.on_message(filters.command('info'))
async def info(_, m: Message):
    await m.reply("Video, Audio, Document >» stream, download links")  
