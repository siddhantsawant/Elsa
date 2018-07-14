#Elsa by Frostmeister


import discord
import math
import time
import googlesearch as gs
import urbandictionary as ud
import random
import asyncio
from discord.ext import commands





###### MATH

class Math:
    def __init__(self , bot):
        self.bot = bot




    @commands.command()
    async def add(self , *args : float):
        "Add nos separated by spaces"
        add=0
        j=len(args)
        for i in range (0,j):
            add=add + args[i]
        await self.bot.say(add)
      

    @commands.command()
    async def sub(self , *args : float):
        """Subtract nos seperated by space"""
        sub=args[0]
        j=len(args)
        for i in range (1,j):
            sub = sub - args[i]
        await self.bot.say(sub)
       
    

    @commands.command()
    async def mult(self , *args : float):
        """Multiply nos separated by space"""
        mult=1
        j=len(args)
        for i in range (0,j):
            mult=mult*args[i]
        await self.bot.say(mult)


    @commands.command()
    async def div(self , *args : float):
        """Divide nos sperated by spaces"""
        div = args[0]
        j= len(args)
        for i in range (1 , j):
            div=div / args[i]
        await self.bot.say(div)      
    


    @commands.command()
    async def fact(self, num : int):
        """Gives the factorial of a no"""
        if num < 100:
            fact=1 
            if num < 0:
                await self.bot.say("Factorial does not exist")
            elif num == 0:
                await self.bot.say("Factorial is 1")
            else:
                for i in range (1 , num +1):
                    fact = fact * i
                await self.bot.say (fact)
        else:
            await self.bot.say("*Calculating.. This might take forever*")
                  





###SETUP

def setup(bot):
    bot.add_cog(Math(bot))
