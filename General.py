#Elsa by Frostmeister

import discord
import math
import time
import googlesearch as gs
import urbandictionary as ud
import random
import asyncio
from discord.ext import commands





####### General

class General:        
    def __init__(self , bot):
        self.bot = bot



    @commands.command()
    async def invite(self):
        """Invite link for Elsa"""
        embed = discord.Embed(title="Elsa's Invite Link ", description="You can invite me to your server" ,color = 0xf5f5dc)
        embed.add_field(name= "Name " , value="Elsa" , inline=True)
        embed.add_field(name= "Prefix for commands" , value = "e! , E!" , inline =True)
        embed.add_field(name ="Invite Link" , value= "   https://discordapp.com/oauth2/authorize?client_id=396540743877001216&scope=bot&permissions=2146958591" , inline=True)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/396540743877001216/85e72bb348b8e0646f25c2926cd7cea5.jpg?size=1024 ")
        embed.set_footer(text = " Feel free to uncheck some permissions " )
        await self.bot.say(embed=embed)






    @commands.command(pass_context=True)
    async def info(self ,ctx, user: discord.Member = None):
        """Gives info about the someone"""
        user = user or ctx.message.author
        try:
            embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find in my bag...", color=0xf5f5dc)
            embed.add_field(name="Username", value=user.name, inline=True)
            embed.add_field(name="Nickname" , value = user.nick , inline = True)
            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="Bot", value=user.bot ,inline=True)
            embed.add_field(name="Status", value=user.status,inline=True)
            embed.add_field(name="Highest role", value=user.top_role)
            embed.add_field(name="Joined Server", value=user.joined_at)
            embed.add_field(name="Joined Discord" , value=user.created_at)
            embed.set_thumbnail(url=user.avatar_url)            
            await self.bot.say(embed=embed)
        except:
            await self.bot.say("Error")
              


               

    @commands.command(pass_context=True, aliases =['svinfo'])
    async def serverinfo(self , ctx):
        """Gives info about the server"""
        embed = discord.Embed(title="{}'s info".format(ctx.message.server.name), description="Here's what I could find in my bag...", color=0xf5f5dc)  
        embed.add_field(name="Servername", value=ctx.message.server.name, inline=True)
        embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
        embed.add_field(name="Verification Level", value=ctx.message.server.verification_level, inline=True)
        embed.add_field(name="Server Region", value=ctx.message.server.region, inline=True)
        embed.add_field(name="Owner" , value=ctx.message.server.owner, inline=True)
        embed.add_field(name="Channels",value=len(ctx.message.server.channels))
        embed.add_field(name="Roles", value=len(ctx.message.server.roles))
        embed.add_field(name="Members", value=len(ctx.message.server.members))
        embed.add_field(name="Emojis", value=len(ctx.message.server.emojis))
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)   
          


###### SETUP

def setup(bot):
    bot.add_cog(General(bot))
