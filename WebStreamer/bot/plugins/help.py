from pyrogram import filters, emoji
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@StreamBot.on_message(filters.command('help'))
async def help(_, m: Message):
    await m.reply("Didn not work? Give a clickdidn't work give a click https://gotalink.herokuapp.com/")
