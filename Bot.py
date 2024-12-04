#MafiaBot by ~ Gytis5089

import discord.utils
import discord
import asyncio
import random
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = ['mafia ', 'Mafia '], intents=discord.Intents.all())
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"mafia help"))
    print('MafiaBot now online.')
    print(f'We are running with {round(client.latency * 100)}ms ping.')

@client.command()
async def create(ctx):
    chinbel = discord.utils.get(ctx.guild.channels, name=str(ctx.author.id))
    if chinbel:
        await ctx.send("Sorry, you already have an active game/channel\nIf you would like to start a new one, just run `mafia delete` in your old game")
    else:
        category = discord.utils.get(ctx.guild.categories, id=893146243675607100)
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            ctx.author: discord.PermissionOverwrite(send_messages=True),
            ctx.author: discord.PermissionOverwrite(view_channel=True)
        }
        channel = await ctx.guild.create_text_channel(str(ctx.author.id), overwrites=overwrites, category=category)
        await channel.send(f"{ctx.author.mention}, welcome to your Mafia game!\nTo add your friends as players, run `mafia add`\nYou can also remove them via `mafia remove`\nHave fun!")

@client.command()
async def delete(ctx):
    if ctx.channel.name == str(ctx.author.id):
        await ctx.channel.delete()
    else:
        await ctx.send("Uh-oh! You can't delete a public channel or others' games")

@client.command()
async def add(ctx, member : discord.Member):
    if ctx.channel.name == str(ctx.author.id):
        await ctx.channel.set_permissions(member, send_messages=True, view_channel=True)
    else:
        await ctx.send("Uh-oh! You can't add people from a public channel or others' games")

@client.command()
async def remove(ctx, member : discord.Member):
    if ctx.channel.name == str(ctx.author.id):
        await ctx.channel.set_permissions(member, send_messages=False, view_channel=False)
    else:
        await ctx.send("Uh-oh! You can't remove people from a public channel or others' games")

@client.command()
async def roles(ctx):
    if ctx.channel.name == str(ctx.author.id):
        ppl = ctx.channel.members
        pplid = [123]
        for el in ppl:
            pplid.append(el.id)
        pplid.remove(123)
        pplid.remove(893148186212958279)
        mafiaid = random.choice(pplid)
        mafia = ctx.guild.get_member(mafiaid)
        try:
            await mafia.send("You are the mafia")
            await ctx.send("The mafia has been notified of their role, if you have not recieved a message, you are a villager.")
        except:
            await ctx.send("I am unable to message the mafia, run the command again to pick a new mafia\n(You might want to change your settings!)")
    else:
        await ctx.send("Uh-oh! You can't set roles for a public channel or others' games")

client.run('ODkzMTQ4MTg2MjEyOTU4Mjc5.YVXPEQ.xb63XDVxGhPWC0u_rEejl4dPtLM')