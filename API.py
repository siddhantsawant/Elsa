#Elsa by Frostmeister



import discord
import math
import time
import googlesearch as gs
import urbandictionary as ud
import chucknorris.quips as q
import xkcd as com
import random
import asyncio
from discord.ext import commands



###### API

class API:

    def __init__(self , bot):
        self.bot = bot



    @commands.command(pass_context=True , aliases = ['g']) 
    async def google(self,ctx,*,query):
        """Google something"""
        try :
            #await self.bot.say("Here's what I could find:") 
            for i in gs.search(query, tld='com', lang='en',     num=1, start=1, stop=2, pause=0.0):
                await self.bot.say(i)
        except Exception as e:
            await self.bot.say(f'Unable to search :{e}')





    @commands.command(pass_context=True , aliases = ['yt']) 
    async def youtube(self,ctx,*,query):
        """Youtube something"""
        try :
            #await self.bot.say("Here's what I could find:") 
            query = 'Youtube' + str(query)
            for i in gs.search(query, tld='com', lang='en',     num=1, start=1, stop=2, pause=0.0):
                await self.bot.say(i)
        except Exception as e:
            await self.bot.say(f'Unable to search :{e}')







    @commands.command()
    async def xkcd(self ,*, number=None):
        """xkcd comic"""
        try:
            if number==None:
                a=com.getRandomComic()
                title=a.getTitle()
                link=a.getImageLink()
                exp=a.getExplanation()
                embed=discord.Embed(title="xkcd", color=0xf5f5dc)
                embed.add_field(name="Title", value=title,inline=False)
                embed.set_footer(text=("For explanation refer to: "+exp))
                embed.set_image(url=link)
                await self.bot.say(embed=embed)
            else:
                number=int(number)
                limit=com.getLatestComicNum()
                if number<1 or number>limit:
                    await self.bot.say("Please enter a number between 1 to 1988")
                else:
                    a=com.getComic(number, silent=True)
                    title=a.getTitle()
                    link=a.getImageLink()
                    exp=a.getExplanation()
                    embed=discord.Embed(title="xkcd", color=0xf5f5dc)
                    embed.add_field(name="Title", value=title, inline=False)
                    embed.set_footer(text=("For explanation refer to: "+exp))
                    embed.set_image(url=link)
                    await self.bot.say(embed=embed)            
        except Exception as e:
            await self.bot.say(f'Unable to fetch comic : {e}')

                   




   


    @commands.command(pass_context = True)
    async def norris(self , ctx,  member: discord.Member = None ):
        """Norris Facts"""    
        if member is not None:    
               text = q.random(member.name)
        else:
             text = q.random()
        embed = discord.Embed(title = ' ' , description = text , color = 0xf5f5dc)
        await self.bot.say(embed = embed)





    @commands.command(pass_context=True, aliases= ['ud'])
    async def urban(self,ctx,*,word):
        """Search something in urbandictionary"""
        embed= discord.Embed(title = word, description='Heres what I could find' , color =0xf5f5dc)
        defi = ud.define(word)
        for d in defi:
            embed.add_field(name='Definition' , value = d.definition , inline = True)
            embed.add_field(name='Example' , value = d.example, inline = True)
            embed.add_field(name= 'Upvotes 👍' , value = d.upvotes , inline = True)
            embed.add_field(name='Downvotes 👎' , value = d.downvotes , inline = True)
            embed.set_footer(text = 'Requested by {}'.format(ctx.message.author))
            embed.set_thumbnail(url = 'https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSZp9CZhLovlcsXWhjiIPjTEwWG7HRmCEYT7NmYDXrGdYUOhfRWjHgbdiU9')
            await self.bot.say(embed=embed)
            break
  
                





##### SETUP

def setup(bot):
    bot.add_cog(API(bot))
