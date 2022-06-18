# bot.py
import os
from speedrun import *
from config import ACCESS_TOKEN, CLIENT_ID, BOT_NICK, BOT_PREFIX, CHANNEL # for importing env vars for the bot to use
from twitchio.ext import commands

class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(
            token=ACCESS_TOKEN,
            #user_id = CLIENT_ID,
            nick = BOT_NICK,
            prefix=BOT_PREFIX,
            initial_channels=[CHANNEL]
            )

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        #print(f'User id is | {self.user_id}')
        await bot.connected_channels[0].send('ready to roll 😎')

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Sending a reply back to the channel is easy... Below is an example.
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')
    
    async def getSpeedrun(self, ctx: commands.Context):
        await ctx.send(f'@{ctx.author.name}, Popeye 2021 WR: ' + getWorldRecord())


bot = Bot()
bot.run()



# bot = commands.Bot(
#     # set up the bot
#     irc_token=os.environ[TMI_TOKEN],
#     client_id=os.environ['CLIENT_ID'],
#     nick=os.environ['BOT_NICK'],
#     prefix=os.environ['BOT_PREFIX'],
#     initial_channels=[os.environ['CHANNEL']]
# )



# if __name__ == "__main__":
#     bot.run()