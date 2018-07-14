#Elsa by Frostmeister




import discord
import math
import time
import googlesearch as gs
import urbandictionary as ud
import random
import asyncio
from discord.ext import commands




####### FUN

class Fun:
    def __init__(self , bot):
        self.bot = bot





    @commands.command(pass_context=True)
    async def ping(self, ctx , ):
        """Pongiee!!"""
        t = await self.bot.say('Pong!')
        ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
        await self.bot.edit_message(t, new_content="🏓 Oops!!! Missed by {}ms".format(int(ms)))




    @commands.command()
    async def snow(self):
        """Get ready for some snow magic"""
        embed = discord.Embed(title="Snow" , description= "Yaay snow lover , here you go" , color = 0xf5f5dc)
        embed.set_image(url=  random.choice ([" https://media.giphy.com/media/5m5IywM2jlKgw/200.gif " ,
        	                                      " http://78.media.tumblr.com/cfe139dd5448933ebadced94bcf54924/tumblr_mzpjretl5U1qdny4ho2_500.gif" ,
        	                                      " https://static.tumblr.com/24b096a0952880d254ef05b7eb651a2c/knjrxw9/QOan75ti8/tumblr_static_tumblr_static_51v6qyaron4044k0o0w44g08c_640.gif" ,
        	                                      "https://media.giphy.com/media/11MYVXYrGPlUBy/giphy.gif" , 
        	                                      "http://78.media.tumblr.com/fcc98dfcad6067713c1e632a109bd2d4/tumblr_mxw2nyxDxq1qhkjhro1_500.gif" , 
        	                                      "http://images6.fanpop.com/image/photos/35500000/Elsa-frozen-35523105-460-338.gif" ,
        	                                      "http://78.media.tumblr.com/a15b36caff632f7409433520a9025fed/tumblr_n0m7mmyPhw1r20o22o6_r1_500.gif" ,
        	                                      "http://images6.fanpop.com/image/photos/35900000/Elsa-disney-frozen-35931894-500-223.gif" ,
        	                                      "https://data.whicdn.com/images/152995019/original.gif" ,
        	                                      "https://img.gifmagazine.net/gifmagazine/images/1221208/original.gif?1479022464" ,
        	                                      "https://media.giphy.com/media/dISKtADOXrKsE/giphy.gif" ,
        	                                      "https://media.giphy.com/media/67C34fCRlMsqk/giphy.gif"
        	                                      
        	                                      ]))
        
        await self.bot.say(embed=embed)      


        


    @commands.command()
    async def choose(self,  *choices : str):
        """Elsa helps you to choose between things"""
        if choices is None:
            await self.bot.say("I select Frost")
        else:
            await self.bot.say(random.choice(choices))
 



    @commands.command(pass_context=True)
    async def emojify(self, ctx, *, msg):
        "Message turns into emojis!!!"
        nums={"0":":zero:","1":":one:","2":":two:","3":":three:","4":":four:","5":":five:","6":":six:","7":":seven:","8":":eight:","9":":nine:"}
        new_msg = ""
        for i in msg:
            if i.isalpha():
                new_msg += (":regional_indicator_" + i.lower()) + ":"
            elif i.isnumeric():
                new_msg += nums[i]
            else:
                new_msg += i
        await self.bot.say(new_msg)
        await asyncio.sleep(2)
        await self.bot.delete_message(ctx.message)




#    @commands.command(pass_context = True)
#    async def xkcd(self, ctx,  no : int = None):
#        """xkcd"""
#        if no is None :
#            no = random.randint(1, 100)
#            await self.bot.say('https://xkcd.com/{}/'.format(no))       
#        else:
#            no = int(no)
#            if no > 1973:
#                await self.bot.say('Please enter a number between 1 and 1973 ')
 #           else:
#                await self.bot.say('https://xkcd.com/{}/'.format(no))     

 
 

 

 
            
   
    @commands.command(aliases = ["8ball"])
    async def ball(self,* , message = None):
        """The 8ball"""
        if message is None:
            await self.bot.say("Nothing here")
        else :
            await self.bot.say(random.choice([  ":8ball: | It is certain " ,
            	                               ":8ball: | It is decidedly so" ,
            	                               ":8ball: | Without a doubt" ,
            	                               ":8ball: | Yes, definitely" ,
            	                               ":8ball: | You may rely on it" ,
            	                               ":8ball: | Most likely" ,
            	                               ":8ball: | As I see it ,yes" ,
            	                               ":8ball: | Yes" ,
            	                               ":8ball: | Signs point to yes" ,
            	                               ":8ball: | Ask again later" ,
            	                               ":8ball: | Reply hazy , Try again" ,
            	                               ":8ball: | Better not tell you now" ,
            	                               ":8ball: | Cannot tell you now" ,
            	                               ":8ball: | Concentrate and ask again" ,
            	                               ":8ball: | Don't count on it" ,
            	                               ":8ball: | My reply is no" ,
            	                               ":8ball: | My sources say no" ,
            	                               ":8ball: | Very doubtful" ,
            	                               ":8ball: | Outlook not so good" ,
            	                               ]))
            	                             
             

    
    @commands.command(pass_context=True , aliases = ["dp", "pfp"])
    async def avatar(self,ctx, user : discord.Member = None ):
        """Gives the avatar of user""" 
        if  user is None:           
            embed = discord.Embed(title="{}'s avatar".format(ctx.message.author) , description="Here's how you look...", color=0xf5f5dc)
            embed.set_image(url= ctx.message.author.avatar_url)
            await self.bot.say(embed=embed)
        else:
            embed = discord.Embed(title="{}'s avatar".format(user.name) , description="Here's how {} looks...".format(user.name), color=0xf5f5dc)
            embed.set_image(url= user.avatar_url)
            await self.bot.say(embed=embed)
   
              
        


        
#    @commands.command(pass_context=True)
#    async def bot(self,ctx, * , message= None):
#        """Gives nature of user"""
#        if self.bot.process_commands("e!bot") == True:
#            return                
#        await self.bot.say(ctx.message.author.bot)
               
     


    @commands.command()
    async def big(self  , emo):
        """Enlarge emoji"""
        emo = emo.split(':')[-1].replace('>' , '')
        await self.bot.say("https://discordapp.com/api/emojis/{}.png".format(emo))





    @commands.command(pass_context=True)
    async def say (self , ctx , * , something=None):
        """Make Elsa say something"""    
        if something is None:
            await self.bot.say("Nothing but cookies here 🍪 🍪 !!!")
        elif '@everyone' in  ctx.message.content.lower():
            await self.bot.say('Ssh.. What are you trying to do')
        else:
            await self.bot.delete_message(ctx.message)
            await self.bot.say(something)
        

      

        
        
    
####Add spam command
 









#### SETUP

def setup(bot):
    bot.add_cog(Fun(bot))

