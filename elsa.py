#Elsa by Frostmeister



import discord
import math
import time
import datetime
import googlesearch as gs
import urbandictionary as ud
import random
import asyncio
import os
from discord.ext import commands



bot = commands.Bot(description=" The Snow Queen ❄️" , command_prefix=("e!","E!"))



################   EVENTS   ###################


@bot.event
async def on_ready():
    files = ['repl','Moderation','Fun','Math','General','API']
    for i in files:
        bot.load_extension(i)

    await bot.change_presence(game= discord.Game(name="with Snow | e!help or E!help",type=0))
    print("---------------------------------")
    print("Logged in as " + bot.user.name)
    print("My id is " + bot.user.id)
    print("---------------------------------")


   




@bot.event
async def on_message(msg : str):   
    if msg.author.bot:
        return
#    elif "elsa" in msg.content.lower():        
#        await bot.send_message(msg.channel , "**Nikhil is Baka**")
#        await bot.process_commands(msg)    
    else:
        await bot.process_commands(msg)     





@bot.event
async def on_message(message):
    if message.channel.id == '396519929974751236': 
        if 'sorry' in str(message.content.lower()):
            await bot.add_reaction(message, '😭')
        elif 'welcome' in str(message.content.lower()):
            await bot.add_reaction(message, '👋')
        else: 
            pass
    await bot.process_commands(message)




@bot.event
async def on_member_join(member):
    if member.server.id == '396519929974751233':
        welcome_channel = bot.get_channel('396519929974751236')
        msg = await bot.send_message(welcome_channel, 'Welcome to the server {} ... Have a great time here..!!! 🎉'.format(member.name))
        await bot.add_reaction(msg, '👋')


@bot.event
async def on_member_remove(member):
    if member.server.id == '396519929974751233':
        remove_channel = bot.get_channel('396519929974751236')
        msg = await bot.send_message(remove_channel, 'Farewell {} ... We will miss you..!!! 👋'.format(member.name))
        await bot.add_reaction(msg, '😭')


#Roles for Spark Server
@bot.event
async def on_message(message) :
    if ctx.message.channel.id == '459725199252783115':
        role_list = ['Snow White', 'Invisible', 'Dark Night','Vampire Red','Dark Tulip', 'Cotton Candy','Dark Orchid', 'Dark Fantasy', 'New Rose', 'Dodger Blue', 'Grey Goose', 'Frosted Lemon', 'Wild Flower', 'Vivid Orange', 'Dark Chocolate', 'Mystic Orange', 'Atomic Pink', 'Mystic Leaf', 'Mermaid', 'Dark Sea', 'Lime Light', 'Pokemon', 'Anime', 'Sensei', 'Kawaii', 'Senpai', 'Kouhai', 'Baka', 'Chan', 'Kun']
        memb = ctx.message.author
        n = len(message)
    
        if message.startswith('iam') :
            role = message[4:n]
            if role in role_list:
                try:
                    await bot.add_roles(memb, discord.utils.get(ctx.message.server.roles, name = role))
                except Exception as error:
                    await bot.send_message(f'Unable to give role : {error}')
                finally:
                    await asyncio.sleep(2)
                    await bot.delete_message(message)
    

        elif message.startswith('iwas') :
            role = message[5:n]
            if role in role_list:
                try:
                     await bot.remove_roles( member , discord.utils.get(ctx.message.server.roles , name = role))
                except Exception as error:
                    await bot.send_message(f'Unable to remove role : {error}')
                finally :
                    await asyncio.sleep(2)
                    await bot.delete_message(message)

        else:
            await asyncio.sleep(1)
            await bot.delete_message(message)

    await bot.process_commands(message)




    



@bot.event
async def on_message(ctx) :
    flag = 1
    list = [ '281823482562478080', '443658561038319616' ]
    if str(ctx.channel.id) in list :
        for a in "abcdefghijklmnopqrstuvwxyz,@$_&-+()/*:;!?.1234567890#" :
            if a in  str(ctx.content.lower()) :
                await asyncio.sleep(0.5)
                await bot.delete_message(ctx)
                flag = 0
        if flag != 0 :
#            pass
            if str(ctx.channel.id) == '281823482562478080':  
                await bot.add_reaction(message = ctx,emoji = "👍")
            elif str(ctx.channel.id) == '443658561038319616':
                emo_y = discord.utils.get(ctx.server.emojis , name = "yes") 
                emo_n = discord.utils.get(ctx.server.emojis , name = "no")
                await bot.add_reaction(message = ctx,emoji = emo_y)                
                await bot.add_reaction(message = ctx ,emoji = emo_n)                        

    if str(ctx.channel.id) == "314799585761427457" and ctx.content[-1] == "?":
        await bot.add_reaction(message = ctx,emoji = "🔼")
        await bot.add_reaction(message = ctx,emoji = "🔽")
    await bot.process_commands(ctx)













############     BOT RUN    ################

bot.run(os.getenv("TOKEN"))

