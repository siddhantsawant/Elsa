#Elsa by Frostmeister



import discord
import math
import time
import datetime
import googlesearch as gs
import urbandictionary as ud
import random
import asyncio
from discord.ext import commands





#############   MODERATION CMDS    ###################





class Moderation:

    def __init__(self , bot):
        self.bot = bot





    @commands.command(pass_context = True , aliases = ['arole' , 'ar'])
    @commands.has_permissions(manage_roles = True)
    async def addrole(self , ctx , member : discord.Member = None , *, role = None):
        """ Add role to a user"""
        try :        
            await self.bot.add_roles( member , discord.utils.get(ctx.message.server.roles , name = role))
            await self.bot.add_reaction(ctx.message , '✅')
        except Exception as error:
            await self.bot.say(f'Unable to add role : {error}')
            
        


    @commands.command(pass_context = True, aliases = ['grole', 'gr'])
    async def getrole(self , ctx, *, role=None):
        """Get a custom role for IU server"""
        role_list = ['Grey', 'Dark', 'Red', 'Green']
        memb = ctx.message.author 
        if ctx.message.server.id != '281793428793196544':
            return
        try:
            if role in role_list:
                await self.bot.add_roles(memb, discord.utils.get(ctx.message.server.roles, name = role))
                await self.bot.add_reaction(ctx.message,'✅' )
            else:
                await self.bot.say("Please enter the role available for grabbing!!!")
        except Exception as error:
                await self.bot.say(f'Unable to give role : {error}')





    @commands.command(pass_context = True , aliases = ['rrole' , 'rr'])
    @commands.has_permissions(manage_roles = True)
    async def removerole(self , ctx , member : discord.Member = None , *, role = None):
        """ Remove role from a user"""
        try :        
            await self.bot.remove_roles( member , discord.utils.get(ctx.message.server.roles , name = role))
            await self.bot.add_reaction(ctx.message , '✅')
        except Exception as error:
            await self.bot.say(f'Unable to remove role : {error}')
        
                
   

    



  
    @commands.command(pass_context = True)
    @commands.has_permissions(kick_members = True)
    async def warn(self , ctx , member : discord.Member = None ,* , reason):
        """Warn a member"""
        try:
            culprit = await self.bot.get_user_info(member.id)
            embed = discord.Embed(title = 'Warning' , description= 'You have been warned by {}'.format(ctx.message.author.name) , color =  0xff4c4c)
            embed.add_field(name= 'Reason:' , value = reason , inline = True)
            embed.set_thumbnail(url = ctx.message.server.icon_url)
            await self.bot.send_message(culprit , embed=embed)
            embed = discord.Embed(title = ' ' , description = str(ctx.message.author.name) + ' warned ' + str(member.name) , color = 0xf5f5dc)
            await self.bot.say(embed = embed)
        except Exception as error:
            await self.bot.say(f'Unable to warn user : {error}')





    @commands.command(pass_context = True ,hidden = True)
    async def log(self , ctx ,* , text):
        """Log"""
        if ctx.message.author.id == '269678631050018826' :
            try :
                text = text.split(',')
                embed = discord.Embed( title = ' ' , description = ' ' , timestamp= datetime.datetime.utcnow() ,color =  0xff4c4c)
                embed.set_author(name = ctx.message.author , icon_url = ctx.message.author.avatar_url)
                embed.add_field(name = 'Case :' , value = text[0] , inline = True)
                embed.add_field(name = 'Action taken:' , value = text[1] , inline = True)
                embed.add_field(name = 'Link : ', value = text[2] , inline = True)
                embed.set_thumbnail( url = 'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSvBHNE1WM58nSumsb-_J7naL9gIujW4tFuPgWg9jIvPatFl-rR0w')  
                embed.set_footer(text = ctx.message.server.name , icon_url = ctx.message.server.icon_url)    
                await self.bot.send_message(discord.Object('426289904125870082'), embed = embed)
                await self.bot.add_reaction(ctx.message , '✅')
            except Exception as error:
                await self.bot.say(f'Unable to add to log : {error} ')
        else : 
            await self.bot.add_reaction(ctx.message , '❌')                    



    

    
     





    @commands.command(pass_context = True)
    @commands.has_permissions(manage_nicknames= True)
    async def nick(self ,ctx , member : discord.Member , * , name : str = None):
        """Change Nickname of a user"""
        name = name or None
        try :
            await self.bot.change_nickname(member , name)
            await self.bot.add_reaction(ctx.message , '✅')
        except Exception as error:
            await self.bot.say(f"Unable to change nickname : {error}")






  

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self , ctx, member: discord.Member):
        """Kick Member"""
        try:
            await self.bot.kick(member)
            await self.bot.say(":boot: Cya, {}. Buh-byee loser!".format(member.name))
        except Exception as error:
            await self.bot.say(f"Unable to kick user : {error}")


    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member):
        """Ban Member"""
        try:
            await self.bot.ban(member)
            await self.bot.say("Buh-byee forever {}. !!!".format(member.name))
        except Exception as error:
            await self.bot.say(f"Unable to ban user : {error}")






    @commands.command(pass_context=True)
    @commands.has_permissions(manage_channels=True)
    async def purge(self, ctx , num ,member: discord.Member = None , channel : discord.Channel = None):
        """Purge messages"""
        channel= channel or ctx.message.channel
        try :
            num = int(num)
            await self.bot.delete_message(ctx.message)
            if member is None:               
                await self.bot.purge_from(channel , limit = num)
                x = await self.bot.say("🗑️ | Messages deleted successfully!!! ")
                await asyncio.sleep(2)
                await self.bot.delete_message(x)
            else:
                await self.bot.purge_from(channel, limit = num , check =(lambda msg: msg.author == member))
                x = await self.bot.say(":wastebasket: | Messages deleted successfully!!! ")
                await asyncio.sleep(2)
                await self.bot.delete_message(x)

        except Exception as error:
            await self.bot.say(f"Unable to delete messages : {error}")
            
 







 
 

 




#### SETUP

def setup(bot):
    bot.add_cog(Moderation(bot))
