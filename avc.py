import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '?')
 
@client.event
async def on_ready():
        await client.change_presence(status=discord.Status.idle, activity=discord.Game('Monitoring activity'))
        print('Bot is ready.')
	
@client.event
async def on_member_join(member):
    print(f'(member) has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'(member) has left a server')
    
@client.command()
async def ping(ctx):
    await ctx.send (f'pong! {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)
    
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    
@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))


    
client.run('NzA0Njg5OTUxNDA4OTE0NTMz.Xqgz3A.VU3fUuQ_KSjhyVFs2RnArnYsZyQ')

  
