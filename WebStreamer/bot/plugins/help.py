from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command('help'))
async def help(_, m: Message):
    await m.reply("Didn not work? Give a clickdidn't work give a click https://gotalink.herokuapp.com/")
