import  discord
from discord import Embed, Member
from discord.ext import *
from discord.ext import commands
import asyncio
from random import *
from typing import *
from math import*
import io
import datetime
from discord.ext import commands

######################################################################################

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "e!", intents=intents)
bot.remove_command("help")

#Ready
@bot.event
async def on_connect():
    print("Le bot est connecté")
    while True:
    	await bot.change_presence(activity=discord.Streaming(name="discord.gg/elexyr22", url="https://www.twitch.tv/elexyr22_"))

######################################################################################

#Erreur
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("``Mmmmmh, j'ai l'impression que cette commande n'existe pas !``")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("``Un argument manque !!``")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("``Vous n'avez pas les permissions pour faire cette commande !!``")
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("``Oups, vous ne pouvez pas utiliser cette commande !!``")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("``Oups, je n'ai pas les permissions nécessaires pour exécuter cette commande !!``")

######################################################################################

@bot.event
async def on_member_update(before, after):
    if "/" not in str(before.activity): #mettre le status qu'il faut avoir | exemple: /elexyr22
        if "/" in str(after.activity): #mettre le status qu'il faut avoir | exemple: /elexyr22
            try:
                guild = bot.get_guild(123) #mettre l'id du serveur concerné
                role = discord.utils.find(lambda r: r.name == 'Soutien', guild.roles) #le nom du rôle que tu veux, pas l'id /!\
                await after.add_roles(role, reason="supporter")
            except Exception:
                pass
    if "/" in str(before.activity): #mettre le status qu'il faut avoir | exemple: /elexyr22
        if "/" not in str(after.activity): #mettre le status qu'il faut avoir | exemple: /elexyr22
            try:
                guild = bot.get_guild(123) #mettre l'id du serveur concerné
                role = discord.utils.find(lambda r: r.name == 'Soutien', guild.roles) #le nom du rôle que tu veux, pas l'id /!\
                await after.remove_roles(role, reason="supporter")
            except Exception:
                pass

######################################################################################

@bot.event
async def on_message(message):
    async def dp(ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.message.author
        userAvatar = member.avatar_url
        await ctx.send(userAvatar)

######################################################################################

bot.run("TOKEN") #Le token de ton bot

######################################################################################
