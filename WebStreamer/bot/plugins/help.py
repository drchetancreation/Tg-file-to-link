from pyrogram import filters
from WebStreamer.bot import StreamBot
from pyrogram.types import Message

@StreamBot.on_message(filters.command('help'))
async def help(_, m: Message):
    await m.reply("Didn not work? Give a click https://gotalink.herokuapp.com/")
