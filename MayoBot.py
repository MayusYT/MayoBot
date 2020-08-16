import importlib

import discord
import json
from discord.ext import commands

from Config import get_token, get_module_names, get_modules
from CoreCog import CoreCog


bot = commands.Bot(command_prefix='?')


@bot.command()
async def restart(ctx):
    if ctx.message.author.id == 218444620051251200:
        await ctx.send("👋  Bye!")
        await bot.logout()
        exit(0)
    else:
        await ctx.send('No permission fam')


@bot.event
async def on_ready():
    print('Logged on as: ', bot.user)


def setup():
    print(get_module_names())
    bot.add_cog(CoreCog(bot))
    load_modules()
    bot.run(get_token())


def load_modules():
    module_list = get_module_names()
    for module in module_list:
        # my_module = importlib.import_module("modules.%s" % module)
        # klass = getattr(my_module, module)
        # bot.add_cog(klass(bot))
        bot.load_extension("modules.%s" % module)


setup()
